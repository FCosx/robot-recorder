# Lenovo recorder executable

**English** | [简体中文](recorder-executable.zh-CN.md)

Normal operators use the existing recorder page and robot/LoRa setup guides. The prepared Lenovo already runs this executable as its background service; no build step or open terminal is required.

The [beta release](https://github.com/FCosx/robot-recorder/releases/tag/lenovo-v0.14.0-beta.1) includes `robot-recorder-linux-x86_64.tar.gz` for maintainers. It contains the tested executable, build/checksum manifest, these notes and compiler/runtime license notices. **It is an update artifact for the prepared recorder, not a blank-machine installer.** It contains no private backend source, operational settings, credentials or recordings.

| Property | Value |
| --- | --- |
| Build | `20261113.1-9f079e13df30` |
| Target | Ubuntu 24.04.5, Linux x86_64, CPython 3.12.3, ROS 2 Jazzy |
| ELF size | 2,472,448 bytes |
| Binary SHA256 | `2b09548d0dedce0e8225c7e3915ab0ea818c63e0023878431dad16f260ae3b88` |
| Installed entry | `/opt/robot-recorder/current/robot-recorder` |

It reuses the installed Python/ROS/public dependencies and external web/setup resources. Pairing, command journal, cloud configuration, upload checkpoints and recordings remain external. Web/LoRa services and version-pinned bandwidth/cloud workers preserve the existing recording-priority barriers. Service-user checks, source-free restart and a real Lenovo reboot passed.

On the prepared recorder, a maintainer can check the installed build and services:

```bash
/opt/robot-recorder/current/robot-recorder --version
sudo systemctl status robot-recorder.service robot-recorder-lora.service \
  robot-recorder-bridge.service --no-pager
```

Do not overwrite or restore live pairing/counters/state when changing application versions. The matching maintainable source and recovery material are retained privately by the maintainer. Compilation is not encryption or guaranteed protection against root/physical reverse engineering. This is not a Windows program or a Pi executable; a Pi needs an ARM64 recorder build and actual-device acceptance.
