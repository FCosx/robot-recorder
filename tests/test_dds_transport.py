"""Buffer setup preserves stronger/custom settings and rolls back persistence failures."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from tools import dds_transport as dds


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.limit=self.root/'limit';self.limit.write_text('212992')
        self.config=self.root/'dds.conf';self.calls=[];self.fail_move=False

    def runner(self,args,**kwargs):
        self.calls.append(args)
        if args[0]=='sysctl':self.limit.write_text(args[-1].split('=')[1])
        elif args[0]=='install':shutil.copyfile(args[-2],args[-1])
        elif args[0]=='mv':
            if self.fail_move:raise subprocess.CalledProcessError(1,args)
            Path(args[-2]).replace(args[-1])
        elif args[0]=='rm':Path(args[-1]).unlink(missing_ok=True)
        return subprocess.CompletedProcess(args,0,'','')

    def configure(self):return dds.configure(self.limit,self.config,self.runner,sudo=[])

    def test_ceiling_persisted_atomically_and_repeat_is_noop(self):
        self.assertTrue(self.configure()['changed'])
        self.assertEqual(int(self.limit.read_text()),dds.KERNEL_CAP)
        self.assertTrue(self.config.read_text().startswith(dds.MARKER+'\n'))
        count=len(self.calls);self.assertFalse(self.configure()['changed'])
        self.assertEqual(len(self.calls),count)

    def test_runtime_only_ceiling_is_persisted_even_when_already_sufficient(self):
        self.limit.write_text(str(dds.KERNEL_CAP))
        self.assertTrue(self.configure()['changed'])
        self.assertEqual(self.limit.read_text(),str(dds.KERNEL_CAP))
        self.assertIn(f'net.core.rmem_max = {dds.KERNEL_CAP}',self.config.read_text())
        self.assertFalse(any(args[0]=='sysctl' for args in self.calls))
        # At boot the kernel starts with its default; the saved sysctl must
        # restore the value needed by the 4 MiB CycloneDDS socket profile.
        self.limit.write_text('212992')
        saved=int(self.config.read_text().split('=')[1].strip())
        self.runner(['sysctl','-w',f'net.core.rmem_max={saved}'])
        self.assertGreaterEqual(int(self.limit.read_text()),dds.KERNEL_CAP)
        count=len(self.calls);self.assertFalse(self.configure()['changed'])
        self.assertEqual(len(self.calls),count)

    def test_higher_runtime_tuning_is_persisted_without_lowering_it(self):
        stronger=32*1024**2;self.limit.write_text(str(stronger))
        self.assertTrue(self.configure()['changed'])
        self.assertEqual(int(self.limit.read_text()),stronger)
        self.assertIn(f'net.core.rmem_max = {stronger}',self.config.read_text())
        self.assertFalse(any(args[0]=='sysctl' for args in self.calls))
        count=len(self.calls);self.assertFalse(self.configure()['changed'])
        self.assertEqual(len(self.calls),count)

    def test_higher_managed_persistent_tuning_is_not_overwritten(self):
        stronger=32*1024**2
        self.config.write_text(f'{dds.MARKER}\nnet.core.rmem_max = {stronger}\n')
        self.limit.write_text(str(dds.KERNEL_CAP));before=self.config.read_text()
        self.assertTrue(self.configure()['changed'])
        self.assertEqual(int(self.limit.read_text()),stronger)
        self.assertEqual(self.config.read_text(),before)
        self.assertEqual([args[0] for args in self.calls],['sysctl'])

    def test_unmanaged_file_is_preserved_when_runtime_ceiling_is_high(self):
        self.limit.write_text(str(32*1024**2));self.config.write_text('user tuning\n')
        with self.assertRaisesRegex(ValueError,'unmanaged'):self.configure()
        self.assertEqual(self.calls,[]);self.assertEqual(self.config.read_text(),'user tuning\n')

    def test_persistence_failure_with_sufficient_runtime_keeps_runtime_unchanged(self):
        self.limit.write_text(str(dds.KERNEL_CAP));self.fail_move=True
        with self.assertRaises(subprocess.CalledProcessError):self.configure()
        self.assertEqual(int(self.limit.read_text()),dds.KERNEL_CAP)
        self.assertFalse(self.config.exists())
        self.assertFalse(self.config.with_name('.dds.conf.new').exists())
        self.assertFalse(any(args[0]=='sysctl' for args in self.calls))

    def test_unmanaged_file_is_preserved(self):
        self.config.write_text('user tuning\n')
        with self.assertRaisesRegex(ValueError,'unmanaged'):self.configure()
        self.assertEqual(self.calls,[]);self.assertEqual(self.config.read_text(),'user tuning\n')

    def test_persist_failure_restores_original_limit(self):
        self.config.write_text(dds.MARKER+'\nold setting\n');self.fail_move=True
        with self.assertRaises(subprocess.CalledProcessError):self.configure()
        self.assertEqual(self.limit.read_text(),'212992')
        self.assertEqual(self.config.read_text(),dds.MARKER+'\nold setting\n')
        self.assertFalse(self.config.with_name('.dds.conf.new').exists())

    def test_profile_preserves_custom_domain_and_interface_choices(self):
        self.assertTrue(dds.write_source_profile(self.root))
        path=self.root/'zenoh/source-cyclonedds.xml';text=path.read_text()
        self.assertIn('Id="any"',text);self.assertIn('min="4MiB"',text)
        self.assertNotIn('NetworkInterface',text)
        path.write_text('<CycloneDDS>operator supplied</CycloneDDS>')
        self.assertFalse(dds.write_source_profile(self.root));self.assertIn('operator supplied',path.read_text())

    def test_authentication_has_no_operation_timeout_and_later_commands_never_prompt(self):
        calls=[]
        def runner(args,**kwargs):
            calls.append((args,kwargs))
            if args==['sudo','-v']:return subprocess.CompletedProcess(args,0,'','')
            self.assertEqual(args[:2],['sudo','-n'])
            return self.runner(args[2:],**kwargs)
        dds.configure(self.limit,self.config,runner,sudo=['sudo'])
        self.assertNotIn('timeout',calls[0][1])
        self.assertTrue(all(kw['timeout']==15 for _,kw in calls[1:]))


if __name__=='__main__':unittest.main()
