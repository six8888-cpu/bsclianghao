# BSC靓号钱包生成器 🚀

高性能BSC链靓号地址生成器，支持前缀、后缀、包含的灵活组合匹配。

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

---

## ⚡ 快速开始

### 本地使用（Linux/macOS）

```bash
# 1. 克隆项目
git clone https://github.com/six8888-cpu/bsclianghao.git
cd bsclianghao

# 2. 安装依赖
pip3 install -r requirements.txt

# 3. 运行（推荐V2版本）
python3 ultra_generator_v2.py
```

**交互式配置**：
- 输入前缀（不需要按回车跳过）
- 输入后缀（不需要按回车跳过）
- 输入包含（不需要按回车跳过）
- 至少需要一个条件

**示例**：
```
前缀: 1780      (地址以0x1780开头)
后缀: 3CffbD    (地址以3CffbD结尾)
包含: 888       (地址中包含888)
```

---

## 🖥️ 服务器部署（一键脚本）

```bash
# 上传并运行部署脚本
curl -o server_deploy.sh https://raw.githubusercontent.com/six8888-cpu/bsclianghao/main/server_deploy.sh
chmod +x server_deploy.sh
./server_deploy.sh

# 或者手动部署
git clone https://github.com/six8888-cpu/bsclianghao.git
cd bsclianghao
pip3 install -r requirements.txt
python3 ultra_generator_v2.py
```

**后台运行**：
```bash
# 使用screen（推荐）
screen -S bsc
python3 ultra_generator_v2.py
# 按 Ctrl+A 然后 D 退出（程序继续运行）

# 恢复会话
screen -r bsc

# 停止程序
# 恢复会话后按 Ctrl+C
```

---

## 💻 Windows版本

下载地址：[GitHub Actions - Artifacts](https://github.com/six8888-cpu/bsclianghao/actions)

1. 访问Actions页面
2. 点击最新的 "Build Windows EXE"
3. 下载 `BSC-Vanity-Generator-Windows-x64.zip`
4. 解压并运行 `BSC-Vanity-Generator.exe`

详见：[windows/README.md](windows/README.md)

---

## 📊 性能参考

| CPU核心 | 预估速度 | 6位地址 | 8位地址 | 10位地址 |
|---------|---------|---------|---------|----------|
| 8核     | 8-12万/s | 1-5分钟 | 1-3小时 | 3-15天 |
| 32核    | 30-50万/s | 10-30秒 | 15-45分钟 | 1-4天 |
| 64核    | 60-90万/s | 5-15秒 | 8-25分钟 | 12小时-2天 |
| 192核   | 180-270万/s | 2-5秒 | 3-8分钟 | 4-12小时 |

*注：实际时间因概率而异，可能更快或更慢*

---

## 🎯 功能特点

### V2增强版（ultra_generator_v2.py）

- ✅ **灵活组合匹配**：前缀+后缀+包含任意组合
- ✅ **实时概率显示**：已完成百分比、预计剩余时间
- ✅ **彩色界面**：进度条、状态、运气提示
- ✅ **详细统计**：最高速度、峰值、平均速度
- ✅ **运气评估**：超幸运🍀 / 正常😊 / 有点慢😰
- ✅ **自动保存**：结果保存到 `ultra_vanity_wallets.txt`

### 简化版（fast_generator.py）

- ✅ 单一模式匹配（前缀或后缀或包含）
- ✅ 适合简单需求

---

## 📝 生成的文件

**ultra_vanity_wallets.txt**：
```
======================================================================
生成时间: 2025-11-17 15:30:45
前缀: 1780
后缀: 3CffbD
包含: (无)
区分大小写: 否
======================================================================

地址: 0x1780abc...def3CffbD
私钥: 0x1234567890abcdef...
```

⚠️ **请妥善保管私钥，不要泄露给任何人！**

---

## 🛠️ 技术栈

- **Python 3.8+**
- **eth-keys**：以太坊密钥管理
- **eth-utils**：以太坊工具库
- **pycryptodome**：Keccak哈希算法

---

## ⚙️ 配置建议

### 进程数设置

**自动检测**（推荐）：
```python
# 程序会自动检测CPU核心数
进程数 = CPU核心数 - 1
```

**手动设置**：
```python
# 运行时输入你想要的进程数
# 建议：进程数 = CPU核心数（或略少）
```

### 服务器推荐配置

| 难度 | 推荐配置 | 预估成本 |
|------|---------|---------|
| 6位地址 | 8核16G | ¥50-100/月 |
| 8位地址 | 32核64G | ¥200-400/月 |
| 10位地址 | 64核128G+ | ¥500-1000/月 |
| 超级靓号 | 192核384G+ | ¥2000+/月 |

---

## 📖 常见问题

### Q: 为什么速度是0/s？
**A**: 更新间隔问题，已在V2版本优化，实时显示准确速度。

### Q: 跑了很久还没出？
**A**: 这是概率问题，就像抛硬币，平均1000次出现一次不代表第1000次就一定出现。运气差可能要2000次，运气好可能100次就出。

### Q: 前缀后缀可以同时用吗？
**A**: 可以！V2版本支持任意组合：
- 只要前缀：后缀和包含按回车跳过
- 只要后缀：前缀和包含按回车跳过
- 全都要：都输入即可

### Q: 大小写敏感吗？
**A**: 运行时会询问，可选择区分或不区分。

### Q: 可以生成多个地址吗？
**A**: 可以，运行时会询问要生成几个。

---

## 🔐 安全提示

1. ⚠️ **私钥管理**：生成的私钥拥有钱包完全控制权，务必安全保存
2. ⚠️ **网络环境**：建议在离线或安全的网络环境下运行
3. ⚠️ **备份重要**：生成的地址文件请及时备份
4. ⚠️ **首次测试**：生成的地址请先小额测试，确认无误后再使用

---

## 📄 开源协议

MIT License - 自由使用，无需授权

---

## 🤝 贡献

欢迎提交Issues和Pull Requests！

---

## 📧 联系方式

- GitHub: [@six8888-cpu](https://github.com/six8888-cpu)
- 项目地址: [https://github.com/six8888-cpu/bsclianghao](https://github.com/six8888-cpu/bsclianghao)

---

**⭐ 如果这个项目对你有帮助，请给个Star支持一下！**
