# Raspberry Pi recorder executable

**English** | [简体中文](recorder-executable.zh-CN.md)

Operators use the prepared Pi's browser UI and robot/LoRa setup guides. Its recorder services start when the Pi boots; no compilation or open terminal is required.

The [Pi v0.15.1 release](https://github.com/FCosx/robot-recorder/releases/tag/v0.15.1) includes `robot-recorder-linux-aarch64.tar.gz` for maintainers. It contains the tested Linux executable, a build/checksum manifest, these notes and compiler/runtime notices. **It is a maintenance update for an already prepared recorder, not an installer for a blank Pi.** Public setup files, installed dependencies, storage configuration and private state are separate.

| Property | Value |
| --- | --- |
| Build | `20261125.cloudmode1-7b90257d62ed` |
| Target | Raspberry Pi 5, Ubuntu 24.04.5, Linux aarch64, CPython 3.12.3, ROS 2 Jazzy |
| ELF size | 2,181,224 bytes |
| Binary SHA256 | `6804c54184b25cc898c8b450247e472a60ea34d296cd05ef0fad967bbf465773` |
| Installed entry | `/opt/robot-recorder/current/robot-recorder` |

The executable reuses the prepared system's Python/ROS libraries and external resources. It contains no operational credentials, pairing journal, cloud configuration or recordings. Saved state stays outside the binary. The Lenovo branch's x86_64 executable cannot run on this Pi; an ARM64 **bridge** package is also a different program from the ARM64 **recorder** executable.

On a prepared recorder, the maintainer can check:

```bash
/opt/robot-recorder/current/robot-recorder --version
sudo systemctl status robot-recorder.service robot-recorder-lora.service \
  robot-recorder-bridge.service --no-pager
```

Before a maintenance update, stop recording, stop queued transfers and preserve the live configuration/state. Verify archive checksums and use the maintainer's deployment procedure. Do not restore an old pairing counter/database over newer live state or operate two recorders with the same paired identity. Apply the matching maintained LAN UI/resources as well as this executable; the archive alone does not update external UI files or the robot-side helper. Existing robot installations receive the helper fixes by rerunning the recorder manual's installer while idle. This archive does not update the separate cloud server.

Native service-user checks, small LAN/LoRa captures, source-free startup and a real Pi reboot passed; see [validation and remaining checks](pi-validation.md). Lenovo-to-Pi sustained checks, cloud stop/resume/priority and the source-robot reboot fix have also passed. These are bounded checks of specific configurations, not a guarantee for every robot or rate. Matching source and recovery material are held privately by the maintainer. Compilation is not encryption or a guarantee against reverse engineering by someone with root or physical access.
