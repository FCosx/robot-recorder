# Robot Recorder — Lenovo beta

**English** | [简体中文](README.zh-CN.md)

The current beta uses a **prepared Lenovo running Ubuntu 24.04 / ROS 2 Jazzy with internal NVMe storage**. Robots send standard ROS topics over Ethernet/Zenoh; users select and record them from a browser. Local recording is the main function; LoRa control and cloud access are optional.

**Demonstrated recording rate: 110 MiB/s for 3 minutes (180 seconds), with no missing messages in the tested configuration.** See [validation and limits](docs/lenovo-validation.md).

Start with the [Recorder User Manual](docs/user-manual.md) ([中文](docs/user-manual.zh-CN.md)). Confirm the recorder's wired address first, start the robot's publishers and finish bridge setup before opening its UI. The current prepared Lenovo is **http://192.168.1.102:8080**. A browser-only computer needs no ROS or bridge installation.

## Included functions

- Select topics and estimate their combined bandwidth on refresh; temporary measurement subscribers stop before recording.
- Change the robot's ROS domain from either UI, saved across reboots; the receiver stays on domain **1**.
- Record MCAP to NVMe, split by size/time, inspect counts/Hz/warnings, download over LAN/Wi-Fi or delete completed recordings.
- Show CPU temperature, free space, recording status and concise connection/data-loss warnings.
- Optional [LoRa remote](docs/lora-remote.md): topic selection, start/stop, splitting, status and recording management. Sensor data stays on Ethernet/Zenoh; the remote needs no recorder IP or site-network access.
- Optional compressed HTTPS cloud upload: Manual/idle Automatic modes, stop/resume, verified-upload badges and recording priority.
- [Cloud website](docs/user-manual.md#cloud-website): private account login, downloads, single/four-topic synchronized timelines with Fast/HD choices, storage display and administrator Trash/Restore/permanent deletion. Automatic deletion stays off.

## Beta packages

Use [Lenovo beta v0.14.0-beta.1](https://github.com/FCosx/robot-recorder/releases/tag/lenovo-v0.14.0-beta.1) for the matching LoRa installer, verified x86_64/ARM64 v2 bridge packages and checksums. The tested Lenovo Linux executable is included as a **maintainer update for the prepared recorder**; see [executable notes](docs/recorder-executable.md). Operators do not build anything.

This branch is the most up-to-date project version. [main](https://github.com/FCosx/robot-recorder/tree/main) retains the stable Pi version; the beta does not replace its release. Public content includes setup tools, LoRa client source, guides, encrypted pairing authorization and the compiled Lenovo asset. Private recorder/cloud backend source, login credentials, decrypted pairing, databases and raw recordings are excluded. Cloning this repository or unpacking the executable does not provision a blank recorder.

Accounts and the pairing passcode are supplied privately by the maintainer. See [third-party notices](THIRD_PARTY_NOTICES.md).
