# 树莓派录制器可执行文件

[English](recorder-executable.md) | **简体中文**

普通用户按手册使用已配置 Pi 的网页和机器人/LoRa 安装步骤。Pi 开机后录制服务自动启动，无需编译或保留终端。

[Pi v0.15.1 发布](https://github.com/FCosx/robot-recorder/releases/tag/v0.15.1)中的 `robot-recorder-linux-aarch64.tar.gz` 供维护者使用，包含已验证的 Linux 可执行文件、构建/校验清单、本说明及编译器/运行库许可。**它是已配置记录器的维护更新，不是空白 Pi 安装器。** 公开安装资源、运行依赖、存储配置及私有状态分别管理。

| 项目 | 值 |
| --- | --- |
| 构建版本 | `20261125.cloudmode1-7b90257d62ed` |
| 目标环境 | Raspberry Pi 5、Ubuntu 24.04.5、Linux aarch64、CPython 3.12.3、ROS 2 Jazzy |
| ELF 大小 | 2,181,224 字节 |
| 二进制 SHA256 | `6804c54184b25cc898c8b450247e472a60ea34d296cd05ef0fad967bbf465773` |
| 已安装入口 | `/opt/robot-recorder/current/robot-recorder` |

程序复用已配置系统中的 Python/ROS 库和外部资源，不包含实际登录凭据、配对记录、云端配置或录制。状态保存在二进制之外。Lenovo 分支的 x86_64 可执行文件不能在此 Pi 使用；ARM64 **桥**与 ARM64 **录制器**也是不同程序。

维护者可在已配置记录器上检查：

```bash
/opt/robot-recorder/current/robot-recorder --version
sudo systemctl status robot-recorder.service robot-recorder-lora.service \
  robot-recorder-bridge.service --no-pager
```

维护更新前先停止录制与排队传输，保存当时的最新配置/状态，核对归档校验和，再按维护者的部署流程操作。不要将旧配对计数或数据库覆盖到更新的运行状态，也不要同时运行两个使用同一配对身份的记录器。维护时还须同步匹配的局域网页面及资源；仅替换本归档不会更新外部网页或机器人端助手。已有机器人在空闲时重跑录制器手册的安装命令，即可获取助手修复。本归档不更新独立云服务器。

实际服务用户检查、小包 LAN/LoRa 录制、无后端源文件启动及真实 Pi 重启均已通过，见[验收与待验证项目](pi-validation.zh-CN.md)。Lenovo → Pi 的持续负载、云端停止／恢复／录制优先及源机器人重启修复也已通过。这些都是特定配置下的有界检查，不保证所有机器人或速率均达到相同结果。匹配源码与恢复资料由维护者私下保存；编译不等于加密，也不能保证拥有 root 或物理设备的人无法逆向。
