# Lenovo 录制器可执行程序

[English](recorder-executable.md) | **简体中文**

普通用户继续使用原录制网页和机器人/LoRa 手册；已经配置好的 Lenovo 会通过后台服务自动运行程序，无需编译或保留终端。

[Beta 发布](https://github.com/FCosx/robot-recorder/releases/tag/lenovo-v0.14.0-beta.1)附 `robot-recorder-linux-x86_64.tar.gz`，供维护者使用，内含已验收程序、构建/校验信息、本说明与编译器/运行时许可。**它是已配置记录器的更新产物，不是空白系统一键安装包。** 不含私有后端源码、运行配置、凭据或录制。

| 属性 | 内容 |
| --- | --- |
| 构建版本 | `20261113.1-9f079e13df30` |
| 平台 | Ubuntu 24.04.5 / Linux x86_64 / CPython 3.12.3 / ROS 2 Jazzy |
| ELF 大小 | 2,472,448 字节 |
| 二进制 SHA256 | `2b09548d0dedce0e8225c7e3915ab0ea818c63e0023878431dad16f260ae3b88` |
| 已安装入口 | `/opt/robot-recorder/current/robot-recorder` |

程序复用已安装 Python/ROS/公开依赖与外部网页/安装资源。配对、命令 journal、云配置、上传状态和录制保持外置。web/LoRa 服务及锁定版本的带宽/云子进程保留录制优先屏障。真实服务用户检查、无私有源码 restart 与实际 Lenovo reboot 均通过。

维护者可在已配置记录器检查版本与服务：

```bash
/opt/robot-recorder/current/robot-recorder --version
sudo systemctl status robot-recorder.service robot-recorder-lora.service \
  robot-recorder-bridge.service --no-pager
```

更换应用版本时，不覆盖或回退现有配对/计数/状态库。匹配的可维护源码与恢复材料由维护者私下保管。编译不是加密或 root/物理访问下的不可逆向保证；这不是 Windows 程序或 Pi 录制程序，Pi 需另做 ARM64 构建和实机验收。
