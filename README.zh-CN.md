# Robot Recorder — Lenovo 备选版本

[English](README.md) | **简体中文**

此分支保留**已配置好的 Lenovo：Ubuntu 24.04 / ROS 2 Jazzy，内部 NVMe 存储**备选方案。机器人通过以太网/Zenoh 传输标准 ROS 话题，用户在浏览器选择并录制。本地录制为主要功能，LoRa 控制与云端为可选增强。**树莓派是主平台；Pi 使用者请从 [main](https://github.com/FCosx/robot-recorder/tree/main) 开始。**

**已验证演示速率：110 MiB/s 连续 3 分钟（180 秒），测试配置下无消息缺失。** 见[验收与限制](docs/lenovo-validation.zh-CN.md)。

先按[使用手册](docs/user-manual.zh-CN.md)确认记录器有线地址，启动机器人发布器并完成桥安装，再打开网页。当前已配置 Lenovo 为 **http://192.168.1.102:8080**。仅打开网页的电脑无需安装 ROS 或桥。

## 功能

- 选择话题，刷新时估算带宽和所选合计；录制前关闭临时测量订阅。
- 在任一 UI 修改并保存机器人 ROS 域，接收端固定为 **1**。
- MCAP 录到 NVMe，按大小/时间切包，查看数量/Hz/告警，通过局域网下载或删除已完成录制。
- 显示 CPU 温度、剩余空间、录制状态及简短连接/丢失风险告警。
- 可选 [LoRa 远控](docs/lora-remote.zh-CN.md)：选话题、启停、切包、状态和录制管理。数据仍经以太网/Zenoh，远端无需记录器 IP 或现场网络。
- 可选 HTTPS 压缩上传：手动/空闲自动、停止/继续、校验完成标记，始终录制优先。
- [云端网页](docs/user-manual.zh-CN.md#云端网页)：个人账号、下载、单话题/四话题同步时间轴、Fast/HD、空间显示及管理员回收站/恢复/永久删除。自动删除仍关闭。

## Beta 安装包

[Lenovo beta v0.14.0-beta.1](https://github.com/FCosx/robot-recorder/releases/tag/lenovo-v0.14.0-beta.1)包含匹配的 LoRa 安装器、经过校验的 x86_64/ARM64 v2 桥包及校验和。另附已验收的 Lenovo Linux 可执行程序，供维护者更新已配置记录器，见[可执行程序说明](docs/recorder-executable.zh-CN.md)。普通用户无需编译。

此分支将 Lenovo 专用手册及历史 beta 与 [main](https://github.com/FCosx/robot-recorder/tree/main) 上的 Pi 主平台分开保留，不表示该快照包含之后的全部通用更新。公开内容包括安装工具、LoRa 客户端源码、手册、加密配对文件和 Lenovo 编译产物；不公开录制/云后端源码、登录凭据、解密配对、数据库或原始录制。克隆仓库或解压可执行包不能在空白设备上完成全部部署。

账号和配对口令由维护者私下提供。见[第三方说明](THIRD_PARTY_NOTICES.md)。
