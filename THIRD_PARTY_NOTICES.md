# Third-party software

Release installers include unmodified pySerial 3.5 Python sources.
Copyright (c) 2001–2020 Chris Liechti. Its BSD-3-Clause license is included in
`lora/licenses/pyserial-LICENSE.txt` and in the installer's `vendor/` directory.
Only encrypted recorder authorization may be published; plaintext pairing credentials and recordings must remain private.
The installer calls the system OpenSSL executable for first-time pairing decryption; OpenSSL is not bundled.

The optional compiled Raspberry Pi ARM64 recorder asset was built with Nuitka 4.3.5. Its archive includes the original compiler license, notice and Runtime Library Exception. CPython, ROS and public runtime dependencies are supplied by the prepared operating system and are not bundled in this asset. Zenoh bridge archives include their own upstream license and notices.
