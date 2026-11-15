# Lenovo beta validation — 2026-11-15

**English** | [简体中文](lenovo-validation.zh-CN.md)

Current setup: Lenovo Ryzen 7 8845HS / 32 GB, Ubuntu 24.04.5 / ROS 2 Jazzy, internal 1-TB NVMe/ext4. Robot: Orin NX / Humble, wired Zenoh 1.10.1 v2; current source domain 99, receiver domain 1. Standard ROS messages are supported.

## Recording result

**110 MiB/s for 3 minutes (180 seconds), with no missing messages in the tested configuration.** This is the current demonstrated recording rate cap, confirmed by the user for documentation on 2026-11-15. The confirmation does not supply raw benchmark logs or a tested binary hash. It is separate from the executable acceptance below, not a software-enforced limit, an intrinsic NVMe limit or a guarantee for other workloads/hardware/longer durations. Historical Pi measurements remain separate.

## Verified functions

| Check | Result |
| --- | --- |
| New robot setup | Verified ARM64/x86_64 bridge packages, Humble/Jazzy/domain detection, persistent bridge/helper; no user compilation/workspace detection |
| Recording/domain/link | Real-sensor captures, splitting, repeated recording, saved LAN/LoRa domain changes and bridge-interruption warnings tested |
| Source-reference check | Earlier six-topic test: RGB 182/182, depth 192/192, scan 128/128 within recorded endpoints; no additional missing/duplicate images |
| Executable acceptance | Build `20261113.1-9f079e13df30`; 15 compiled modules; 240 backend tests; LAN/LoRa control, split/details/delete, downloads and small compressed uploads passed |
| Recording priority | A deliberately blocked owned upload worker was reaped in 0.313 s before capture; upload resumed and verified afterward |
| Capture integrity | Two small executable captures: 186 messages, 9 independent split boundaries; payload/source times matched, zero internal gaps/duplicates |
| Source-free startup | Restart and actual Lenovo reboot passed; recorder/LoRa/bridge automatically active, source/cloud/radio reconnected; 25 setup routes matched |
| Preservation | 14 existing recordings, static settings, pairing/journal and original upload state preserved |
| Cloud | Full timelines and synchronized seeking; storage/Trash/Restore/permanent deletion; simplified account creation/reset/delete; administrator self-password change |

Cloud preview work fixed preparation timeout handling, repeated full-index downloads and whole-selection fallback. A real 120-second four-topic JPEG/IMU/scan recording's Fast preparation fell from 129.293 s to 26.906 s in the recorded tests. A separate older raw-image field bag's cached playback startup did **not** improve; preparation timing is not a universal first-play guarantee. Fast/HD remain sampled previews; original downloads are unchanged.

Beta public checks: 125 Python tests discovered, **115 passed and 10 private-backend checks skipped**; **4 JavaScript test files passed**. Installer contents, unchanged encrypted pairing, isolated pairing/counter preservation, both bridge packages, compiled-binary identity, 55 local links and 70 shell examples passed release checks. The 240 backend tests above belong to earlier private executable acceptance, not this public subset.

## Limits

Warnings identify reported loss or risks; their absence does not prove complete publisher delivery. The small functional captures above check their recorded source endpoints and do not replace the separate 180-second result. No new disk-full, power-loss or long-distance radio acceptance is claimed. Dedicated 2D scan design and extensive edge-case tuning remain future work. Automatic cloud deletion stays off; independent cloud backup is outside this beta.

Private backend source/credentials/pairing/state/bags remain unpublished. The compiled asset needs a maintainer-prepared Ubuntu 24.04 x86_64/Jazzy recorder, external resources and installed dependencies; compilation is not encryption or a guarantee against reverse engineering. A Pi needs its own ARM64 recorder build and device validation; the ARM64 bridge asset is not a Pi recorder executable. This beta does not replace the stable Pi release.
