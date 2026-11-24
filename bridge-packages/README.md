# Corrected Zenoh bridge packages — Pi main

The prepared Pi serves verified x86_64 and ARM64 source-bridge packages for ROS 2 Humble/Jazzy (glibc 2.35 or newer). Users run the manual's setup command; no compilation is required. Matching archives are included in [Pi v0.15.0](https://github.com/FCosx/robot-recorder/releases/tag/v0.15.0). The catalog pins upstream Zenoh 1.10.1, the combined patch, archive checksums and binary checksums. Archives include BUILD.json and upstream notices.

**route-listener-v2** retains the listener-lifetime duplication correction and uses live VOLATILE history for Image/CompressedImage routes. Calibration/TF and other non-image retained topics keep their semantics. Source setup provisions bounded 4-MiB DDS receive buffers and a sufficient kernel ceiling, preserving stronger/custom settings and the robot's routes/workspace.

Both architecture packages match those previously validated with the Lenovo/Orin setup; the Pi migration reused the ARM64 receiver and passed bounded capture/reboot checks. This is not a guarantee of complete delivery or performance on every robot. The receiver backend and its own DDS profile are prepared separately by the maintainer. A bridge archive is not the Pi recorder executable or a blank-recorder installer. The Lenovo branch keeps its separate historical release.
