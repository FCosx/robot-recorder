# Pi validation and remaining checks — 2026-11-26

**English** | [简体中文](pi-validation.zh-CN.md)

Primary recorder: Raspberry Pi 5 Model B Rev 1.1 / 8 GB, Ubuntu 24.04.5 / ROS 2 Jazzy, active cooler, native ARM64 recorder, Kingston A400 480 GB ext4 SSD over USB 3/UAS and 1-Gbit Ethernet. Lenovo is the robot/source; an operator laptop only opens the UIs and performs maintenance. The Pi receives on domain **1**; the robot source domain is independently selected and saved. Standard ROS messages are supported.

## Completed acceptance

The following checks ran on 24–25 November; release packaging on 26 November did not repeat the long load tests.

| Check | Result |
| --- | --- |
| Native delivery | Current build `20261125.cloudmode1-7b90257d62ed`; all 15 compiled modules and ROS/dependency checks pass. Matching LAN/LoRa resources were deployed. |
| Sustained 110 MiB/s | Lenovo → Pi, 512 KiB × 220 Hz, 180-second measurement window: **39,600 / 39,600** source messages saved; peak CPU **68.3°C**; seven MCAP files and six continuous split boundaries. |
| Sustained 80 MiB/s | Same path, 160 Hz, 300 seconds: **48,000 / 48,000** saved; peak CPU **67.75°C**; eleven MCAP files and ten continuous boundaries. |
| Storage and integrity | No new USB disconnect/reset, UAS, I/O, ext4 or power errors in those runs. Payload hashes, source sequence/time references and MCAP CRC checks pass; no duplicates or bad payloads. |
| Real sensor recording | D435i RGB, depth, organized coloured point cloud, camera calibration and static transforms: **15.016 s**, **1,126 messages**; 225 per main stream, about 14.99 Hz. Message layouts, CRCs and matched source header timestamps pass. Compressed upload passed full checksum verification; three preview indexes were verified. |
| Cloud workflow | Small real-device compression/upload Stop via LAN and LoRa, multipart resume, full download integrity, isolated idle Automatic and recording priority pass. An active upload worker stops before capture; it can continue afterward. |
| Both UIs and domains | LAN/LoRa selected-topic recording, size/time splitting, details and source-domain changes pass; Pi domain remains 1. Existing pairing and increasing command counters are preserved. |
| Startup | Pi reboot restores SSD and native services. After the persistent-buffer fix, an actual Lenovo reboot automatically reconnects **before SSH sign-in**; receive limit remains 8 MiB, unit enabled/active, no service restart increments, post-boot capture **40 / 40** messages. |
| Connection status | Unique helper node names remove the reproduced false-disconnection case. Real source-bridge interruption still produces a warning; recovery and domain changes pass. |
| Cloud mode fix | Both UIs can return to Manual with unknown/unreachable cloud status, including during capture. Enabling Automatic and new uploads still require cloud reachability; recording priority and Stop remain enforced. |

These are bounded measurements of specific configurations, not an absolute throughput ceiling or indefinite loss-free guarantee. Including warmup/tail, the sustained runs saved 41,361/41,361 and 49,281/49,281 messages. At 110 MiB/s the near-network-capacity risk warning correctly remains even though the independent source comparison found no loss. The earlier operator-laptop-source run lost 84/39,600 messages; the source computer/profile/path/domain also changed, so the newer result does not isolate cooling or one hardware component as the cause.

The RealSense source header timestamps align exactly in that driver configuration; this does not establish independent hardware-clock accuracy or completeness for arbitrary sensors. Invalid scene depth remains invalid in recordings. Real sensor data was retained; owned synthetic test bags were removed after their reference evidence was saved.

The reboot test also observed early clock-skew warnings until the existing NTP service synchronized. The 40-message check ran afterward. No clock policy was changed, and time-sensitive recording during that unsynchronized interval is not validated.

The bridge retains its listener-lifetime duplication fix and v2 image-history handling. Setup persists the DDS receive-buffer ceiling even if the runtime value is already sufficient, preserving higher managed limits. Temporary bandwidth readers must close and acknowledge before capture. Warnings detect reported loss or known pressure/interruption risks; absence of a warning is **not** proof of complete delivery for arbitrary publishers.

Cloud supports verified indexed-Zstandard uploads, individual accounts, downloads, single/four-topic full timelines and seeking, Fast/HD, depth colours and interactive 3D point clouds. Previews are sampled copies. Storage display and administrator Trash/Restore/permanent deletion are available; automatic deletion remains off. Preview preparation may still take time on a first read or slow network. No independent bag backup is promised.

## Release checks

120 public Python tests passed; 10 tests requiring the private backend were skipped. All four JavaScript suites passed. Actual public LoRa first installation and update, encrypted-pairing identity, preserved local counters, embedded-guide/runtime agreement, both bridge archive hashes/architectures and temporary x86_64 bridge installation are checked. The Pi ELF matches the privately archived, deployed build. Public files and expanded archives are checked for private credentials, operational state and excluded backend source. These packaging checks do not run publishers or modify recordings/cloud objects.

## Remaining validation

1. **Robot and field workflow:** fresh Humble/ARM64 installation and representative sensors; operator access over reachable Wi-Fi and NoMachine, including download destinations. The released first-time bridge commands have already passed on Lenovo/Jazzy x86_64; this does not replace Orin/Humble field acceptance.
2. **Real-distance LoRa:** command/status reliability, reconnection and topic/catalog latency at the intended site. A large catalog can be slow at the current air rate. One-second polling is a wait after replies, not a one-second delivery or one-mile range guarantee.
3. **Longer/fault-edge evidence:** arbitrary sensor completeness, startup before clock synchronization, abrupt power/cable failure and independently re-reading the low-space auto-stop bag remain outside the completed checks. No destructive full-disk or power-cut test was run.

## Optional later work

Dedicated 2D LaserScan display, faster initial preview preparation, estimates for sparse/bursty topics and the previously observed robot LiDAR shutdown timeout. Automatic cloud retention, independent backups, deeper physical-device protection and a blank-Pi provisioning installer require separate decisions; they are not enabled by this release.
