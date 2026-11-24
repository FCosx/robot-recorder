# Pi validation and remaining checks — 2026-11-24

**English** | [简体中文](pi-validation.zh-CN.md)

Primary recorder: replacement Raspberry Pi 5 Model B Rev 1.1 / 8 GB, Ubuntu 24.04.5 / ROS 2 Jazzy, native ARM64 recorder, ext4 SSD and 1-Gbit Ethernet. The prepared bundle retains its Pi address and stored recordings. The receiving DDS domain is fixed at 1; the robot's source domain is a separate persistent UI setting. Standard ROS messages are the supported scope.

## Completed acceptance

| Check | Evidence |
| --- | --- |
| Native delivery | Build `20261124.pi1-9f079e13df30`; 15 compiled modules and ROS/dependency checks pass under the recorder account |
| LAN capture | 58 messages across 3 MCAP files in a bounded 4-KiB/intended 10-Hz test |
| LoRa capture | Selected-topic Start/Stop/details; 110 messages across 6 MCAP files |
| Integrity | All 168 messages passed source payload/time/hash and MCAP CRC checks; zero internal sequence gaps, duplicates or decreases; 7 contiguous split edges |
| Recording priority | In one LAN check, temporary-reader STOP confirmation took about 0.0156 s; no measurement/compression/upload activity during capture |
| Startup | Real reboot restores SSD mount, native recorder, receiving bridge and LoRa agent; source test bridge, cloud and radio reconnect |
| Preserved data | Seven moved bags / 48 files checked for exact SHA256 and integer nanosecond modification times; earlier SSD bags retained |
| User-facing state | Recording details and migrated Uploaded badges display correctly; current cloud connection is available in Manual mode |

These are small functional checks. Sequence comparisons cover only the first-to-last recorded source endpoints and are not proof of source data before or after them. Existing historical throughput results are separate; this release does not claim a new sustained-rate or thermal result for the replacement board.

The shared bridge retains the listener-lifetime duplication correction and v2 live Image/CompressedImage history handling. Source setup provisions bounded DDS receive buffers while preserving custom settings. The receiver also retains bandwidth-coordinator recovery, clean source-offline shutdown and concise UDP/network-loss risk indications. Starting capture still requires the robot to confirm temporary measurement subscribers have closed. Warnings do not prove complete publisher delivery or provide exact missing-source counts for arbitrary sensors.

The already deployed cloud supports compressed verified uploads, accounts, single/four-topic full-recording playback and seeking, Fast/HD, depth colour maps and interactive XYZ point clouds. Cloud originals/downloads stay unchanged. Storage display and administrator Trash/Restore/permanent deletion are available; automatic deletion stays off. Initial preview preparation or buffering can still take time, especially for large clouds or slow networks.

## Public release checks

For this release, 125 Python tests were discovered: 115 passed and 10 checks requiring the private backend were skipped. All four JavaScript test files passed. The actual public LoRa bundle passed first installation and update checks with isolated pairing/counter preservation; its embedded guides/runtime match the repository. Both bridge archives, manifests and architecture headers match their checksums; the x86_64 bridge also passed a real temporary installation/version check. The Pi ELF matches the already accepted ARM64 build. Public-source/asset exclusion checks, 38 local links/anchors and 38 shell examples passed. No radio, cloud object or production recorder was changed by these release checks.

## Remaining validation, in order

1. **Replacement-Pi sustained recording:** a focused longer run around the previously demonstrated operating range, checking source counts, payloads, SSD/USB errors, CPU temperature and fan behaviour. This is still needed after changing boards/cooling.
2. **Small end-to-end cloud check on this Pi:** compress/upload, stop/resume, full download integrity and starting recording during a queued transfer. Cloud features passed earlier-device tests; the migration itself checked connectivity and preserved upload state, not a new upload.
3. **Fresh robot and field validation:** follow the released commands on an available Humble/Jazzy robot, verify domain changes/reboot recovery and representative sensors. Check NoMachine access and download destinations in the real operator workflow.
4. **Long-distance LoRa:** measure command/status reliability and topic/list latency at the actual site. A one-mile range or one-second end-to-end refresh is not guaranteed by the selected polling interval.

## Optional later development

Dedicated 2D LaserScan display, further preview-startup optimisation, bandwidth-estimate refinement for sparse/bursty topics and investigation of the observed robot LiDAR shutdown timeout. Automatic cloud-retention rules and deeper physical-device protection are separate design choices, not enabled features or release claims. A full blank-Pi installer is not supplied by this maintenance release.
