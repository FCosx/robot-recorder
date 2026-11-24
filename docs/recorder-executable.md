# Raspberry Pi recorder executable

**English** | [简体中文](recorder-executable.zh-CN.md)

Operators use the prepared Pi's browser UI and robot/LoRa setup guides. Its recorder services start when the Pi boots; no compilation or open terminal is required.

The [Pi v0.15.0 release](https://github.com/FCosx/robot-recorder/releases/tag/v0.15.0) includes `robot-recorder-linux-aarch64.tar.gz` for maintainers. It contains the tested Linux executable, a build/checksum manifest, these notes and compiler/runtime notices. **It is a maintenance update for an already prepared recorder, not an installer for a blank Pi.** Public setup files, installed dependencies, storage configuration and private state are separate.

| Property | Value |
| --- | --- |
| Build | `20261124.pi1-9f079e13df30` |
| Target | Raspberry Pi 5, Ubuntu 24.04.5, Linux aarch64, CPython 3.12.3, ROS 2 Jazzy |
| ELF size | 2,181,224 bytes |
| Binary SHA256 | `ad5d99db50b27202fd51bfb3b6e4aad41f2905ac8b8c3112bbe84a5e51654e54` |
| Installed entry | `/opt/robot-recorder/current/robot-recorder` |

The executable reuses the prepared system's Python/ROS libraries and external resources. It contains no operational credentials, pairing journal, cloud configuration or recordings. Saved state stays outside the binary. The Lenovo branch's x86_64 executable cannot run on this Pi; an ARM64 **bridge** package is also a different program from the ARM64 **recorder** executable.

On a prepared recorder, the maintainer can check:

```bash
/opt/robot-recorder/current/robot-recorder --version
sudo systemctl status robot-recorder.service robot-recorder-lora.service \
  robot-recorder-bridge.service --no-pager
```

Before a maintenance update, stop recording, stop queued transfers and preserve the live configuration/state. Verify archive checksums and use the maintainer's deployment procedure. Do not restore an old pairing counter/database over newer live state or operate two recorders with the same paired identity. This archive does not update the separate cloud server.

Native service-user checks, small LAN/LoRa captures, source-free startup and a real Pi reboot passed; see [validation and remaining checks](pi-validation.md). A fresh sustained-throughput/thermal test on this replacement board remains pending. Matching source and recovery material are held privately by the maintainer. Compilation is not encryption or a guarantee against reverse engineering by someone with root or physical access.
