# Robot Recorder

**English** | [简体中文](README.zh-CN.md)

A ROS 2 data recorder for robot experiments. Robots send topics to a Raspberry Pi over Ethernet and Zenoh. Users select topics and control recording through a browser on the local network; MCAP files are saved on the Pi.

**Raspberry Pi is the primary recorder platform.** Start with this `main` branch and its Pi user manual below. Released installers are versioned separately from the maintained device software.

## Main features

- Discover and select ROS 2 topics to record; set the robot bridge ROS domain from either UI, saved across reboots.
- Estimate topic bandwidth on refresh; measurement subscribers close before recording starts.
- Start and stop recording; split MCAP files by size or duration.
- Inspect recording size, duration, topic message counts and average Hz; download or delete recordings.
- Monitor recording status, free space, CPU temperature and brief warnings.
- Optional HTTPS/S3 cloud uploads: indexed MCAP Zstandard compression, manual/idle automatic modes and verified-upload badges; recording takes priority.
- Cloud login, downloads, single/four-topic synchronized playback, Fast/HD images, depth colouring and interactive 3D point clouds.
- Access the robot's browser through NoMachine when an operator laptop cannot stay wired to the switch.

## Latest fixes

- Persist DDS receive-buffer setup even when a temporary value is already sufficient; the Lenovo robot reconnects after reboot without signing in.
- Give each bandwidth helper a unique ROS node identity to avoid false robot-disconnection reports.
- Allow returning to Manual upload when cloud status is unknown or unavailable; enabling Automatic and starting uploads still require cloud access.

## First-time setup

**Start with the [Recorder User Manual](docs/user-manual.md) ([中文](docs/user-manual.zh-CN.md)).** It provides copy-and-paste commands for the normal workflow, followed by troubleshooting for special cases:

1. Connect the robot, prepared Pi and router LAN port to the same Ethernet switch.
2. Start the robot's normal ROS publishers; the installer detects ROS Humble/Jazzy and the initial source domain automatically, without loading a workspace.
3. Run the manual's installer once: prebuilt x86_64/ARM64 bridge, automatic ROS settings, startup service and a combined setup check.
4. Open the new **Robot Recorder** application shortcut or `http://192.168.1.182:8080`, the Pi's reserved wired address in the supplied bundle. Select topics and record; inspect, download or delete recordings afterward.

The Pi must already be configured by the maintainer; the robot needs ROS 2 Humble or Jazzy. Missing ROS dependencies require internet access; the bridge package downloads from the Pi. No user compilation is required. Routine local recording does not. You do not need to clone this repository first.

## Everyday use

Power on the bundle and robot, start the robot's publishers, then open **http://192.168.1.182:8080** in a browser that can reach the Pi over Ethernet or Wi-Fi. Alternatively, connect to the robot's desktop through NoMachine and use its browser. The robot bridge starts automatically and reconnects when the Pi is available; no terminal needs to stay open. A browser-only computer needs no ROS or bridge installation.

Downloads go to the computer running the browser: using the robot's browser through NoMachine saves to the robot. To preview or download on your own device, upload from the Pi to the cloud and open the cloud in that device's own browser.

Check **Robot ROS domain** against the robot publishers, then select topics and begin recording. Changes can be applied while idle and are saved on the robot. The Pi receiver stays on domain 1. After stopping, wait for finalization before inspecting the result. If the bundle address changes or a robot has a fixed Ethernet address on a different subnet, follow the manual's troubleshooting section. Local-name access is an optional shortcut.

## Optional cloud access

The cloud website is **https://154.8.234.96**. Upload completed recordings directly from the Pi, then use any internet-connected computer to sign in, preview and download cloud copies. Single-topic and synchronized views share a draggable full-recording timeline. Fast/HD previews are sampled copies; original downloads stay unchanged. Administrators can move cloud recordings to Trash, restore them or permanently delete them. Automatic deletion stays off. Local recording works independently of the cloud.

Ask the project maintainer for your individual account; login details are shared privately. Follow the [cloud website guide](docs/user-manual.md#cloud-website) ([中文](docs/user-manual.zh-CN.md#云端网页)).

## Optional enhancement: LoRa remote control

For control outside the local network, add compatible USB LoRa radios and an operator laptop. Follow the [LoRa Remote Guide](docs/lora-remote.md) ([中文](docs/lora-remote.zh-CN.md)). It provides topic selection, Start/Stop, status and brief recording management. Sensor data continues over the robot-to-Pi Ethernet/Zenoh link.

The LoRa laptop can be installed offline and operated without the Pi's IP or access to the site network. GitHub downloads require internet; the maintainer supplies the first-time pairing passcode privately. The installer adds **Robot Recorder LoRa** to the application menu; opening it starts/reuses one background controller. No terminal needs to stay open. Status polling waits one second after each reply by default. The LoRa page does not download recordings.

## Repository contents

The [Pi release v0.15.1](https://github.com/FCosx/robot-recorder/releases/tag/v0.15.1) includes the matching LoRa installer, verified v2 ARM64/x86_64 bridge packages, manifest and checksums. The compiled **Pi ARM64** recorder is a maintenance update for an already prepared Ubuntu 24.04/Jazzy recorder; see [executable notes](docs/recorder-executable.md). It does not provision a blank Pi. Operators do not build anything.

Public contents include guides, robot bridge/setup tools, LoRa source and encrypted pairing authorization. Private recorder/cloud backend source, login credentials, decrypted pairing, databases, raw recordings and private build archives remain excluded. Standard ROS message types are supported; custom types remain outside scope.

The robot bridge launcher also starts a small rate helper. Refreshing either UI takes one short robot-local snapshot; recording waits for temporary readers to close. Existing robots receive the helper and automatic startup by rerunning the manual's setup command while the recorder is idle.

The LoRa installer includes pySerial 3.5; see [Third-party notices](THIRD_PARTY_NOTICES.md).

## Validation and remaining work

See [Pi validation and remaining checks](docs/pi-validation.md) ([中文](docs/pi-validation.zh-CN.md)). Lenovo-to-Pi tests saved 110 MiB/s for three minutes and 80 MiB/s for five minutes with no missing messages in the measured windows; SSD/USB checks passed and CPU peaks were 68.3°C/67.75°C. These are measured configurations, not a universal loss-free limit. Small cloud stop/resume/priority checks and a real RGB/depth/point-cloud capture also passed. New Humble/ARM64 field setup, NoMachine/Wi-Fi access and long-distance LoRa still need validation.
