# GitHub仓库使用指南

## 🔗 仓库地址
https://github.com/six8888-cpu/bsclianghao

---

## 🚀 推送成功后的操作

### 1. 访问你的GitHub仓库
```
https://github.com/six8888-cpu/bsclianghao
```

### 2. 查看GitHub Actions（自动打包Windows EXE）

#### 步骤：
1. 点击仓库顶部的 **"Actions"** 标签
2. 你会看到 "Build Windows EXE" workflow
3. 点击最新的workflow运行记录
4. 等待打包完成（约5-10分钟）
   - 🟡 黄色圆圈 = 正在运行
   - 🟢 绿色对勾 = 成功
   - 🔴 红色叉号 = 失败

#### 下载Windows EXE：
1. 打包成功后，向下滚动到 **"Artifacts"** 部分
2. 点击 **"BSC靓号生成器-Windows-x64"** 下载
3. 解压ZIP文件，得到 `BSC靓号生成器.exe`
4. 双击运行即可使用

---

## 📁 仓库文件结构

```
bsclianghao/
├── 核心程序
│   ├── fast_generator.py          - 极速版
│   ├── ultra_generator.py         - 超级版
│   └── ultra_generator_v2.py      - V2增强版（推荐）
│
├── windows/                        - Windows专用文件夹
│   ├── ultra_generator_windows.py - Windows版本
│   ├── build.bat                  - 打包脚本
│   └── 相关文档
│
├── 部署脚本
│   ├── auto_deploy.sh             - 服务器自动部署
│   └── 一键部署_192核.sh          - 一键部署
│
└── 完整文档
    ├── README.md                  - 项目介绍
    ├── 文件说明.md                - 完整说明
    ├── V2版本说明.md              - V2新功能
    └── 其他文档
```

---

## 🎯 主要功能

### V2版本新功能
- ✅ **灵活组合匹配** - 前缀+后缀+包含任意组合
- ✅ **实时概率显示** - 知道找到的可能性
- ✅ **彩色界面** - 美观清晰
- ✅ **运气提示** - 😎 才刚开始 → 🔥 马上就要出了
- ✅ **详细统计** - 峰值速度、运气评估

### 使用示例
```bash
# Linux/macOS
python3 ultra_generator_v2.py

# 输入示例：
前缀: 1780        （或按回车跳过）
后缀: 3CffbD      （或按回车跳过）
包含: 888         （或按回车跳过）
```

---

## 📥 克隆仓库到本地

### 方式1：HTTPS
```bash
git clone https://github.com/six8888-cpu/bsclianghao.git
cd bsclianghao
```

### 方式2：SSH（推荐）
```bash
git clone git@github.com:six8888-cpu/bsclianghao.git
cd bsclianghao
```

### 方式3：下载ZIP
1. 访问仓库页面
2. 点击绿色 "Code" 按钮
3. 选择 "Download ZIP"
4. 解压使用

---

## 🔄 更新代码

### 如果你修改了代码
```bash
cd /Users/xiaowu/tst

# 1. 查看修改
git status

# 2. 添加修改
git add .

# 3. 提交
git commit -m "描述你的修改"

# 4. 推送到GitHub
git push origin main
```

### 如果从其他电脑拉取最新代码
```bash
cd bsclianghao
git pull origin main
```

---

## 🌟 GitHub仓库设置

### 设置为Public（公开）
1. 进入仓库
2. 点击 "Settings"
3. 向下滚动到 "Danger Zone"
4. 点击 "Change visibility"
5. 选择 "Make public"

### 添加README徽章
在 `README.md` 顶部添加：

```markdown
[![Build Windows EXE](https://github.com/six8888-cpu/bsclianghao/actions/workflows/build-windows.yml/badge.svg)](https://github.com/six8888-cpu/bsclianghao/actions/workflows/build-windows.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
```

### 添加Topics（标签）
1. 点击仓库右侧的 ⚙️（齿轮图标）
2. 添加标签：
   - `bsc`
   - `vanity-address`
   - `wallet-generator`
   - `python`
   - `cryptocurrency`

---

## 📊 查看项目统计

### Insights
访问：https://github.com/six8888-cpu/bsclianghao/pulse

可以看到：
- 提交历史
- 代码频率
- 贡献者
- 流量统计

### Releases
如果你想发布版本：

1. 点击 "Releases"
2. 点击 "Create a new release"
3. 输入版本号（如：v2.0）
4. 填写更新说明
5. 上传文件（如编译好的EXE）
6. 点击 "Publish release"

---

## 🐛 Issues（问题追踪）

### 创建Issue
如果发现bug或有新功能建议：

1. 点击 "Issues" 标签
2. 点击 "New issue"
3. 填写标题和描述
4. 提交

### Issue模板（可选）
创建 `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug报告
about: 报告一个问题
---

**问题描述**
简要描述问题

**重现步骤**
1. 
2. 
3. 

**预期行为**
应该发生什么

**实际行为**
实际发生了什么

**环境**
- OS: 
- Python版本: 
- 版本: 

**截图**
如果有的话
```

---

## 🔒 安全注意事项

### ⚠️ 不要提交的内容
- ❌ 密码和私钥
- ❌ API密钥和Token
- ❌ 服务器IP和凭证
- ❌ 生成的钱包文件

### ✅ .gitignore已配置
项目已包含 `.gitignore`，会自动忽略：
- 生成的钱包文件 (`*_vanity_wallets.txt`)
- 配置文件 (`*_config.sh`, `*.secret`)
- Python临时文件
- 系统文件

---

## 📱 GitHub手机App

### 下载
- iOS: https://apps.apple.com/app/github/id1477376905
- Android: https://play.google.com/store/apps/details?id=com.github.android

### 功能
- ✅ 查看代码
- ✅ 查看Issues和PR
- ✅ 查看Actions运行状态
- ✅ 接收通知

---

## 🤝 协作

### 如果要邀请其他人协作
1. 进入仓库
2. 点击 "Settings"
3. 点击 "Collaborators"
4. 点击 "Add people"
5. 输入GitHub用户名
6. 发送邀请

---

## 📚 相关链接

### 文档
- README: https://github.com/six8888-cpu/bsclianghao/blob/main/README.md
- 文件说明: https://github.com/six8888-cpu/bsclianghao/blob/main/文件说明.md
- V2版本说明: https://github.com/six8888-cpu/bsclianghao/blob/main/V2版本说明.md

### Actions
- Workflows: https://github.com/six8888-cpu/bsclianghao/actions
- Build Windows EXE: https://github.com/six8888-cpu/bsclianghao/actions/workflows/build-windows.yml

### 代码
- 主要代码: https://github.com/six8888-cpu/bsclianghao/tree/main
- Windows版本: https://github.com/six8888-cpu/bsclianghao/tree/main/windows

---

## 🎉 完成！

你的BSC靓号生成器现在已经在GitHub上了！

### 下一步：
1. ✅ 访问仓库页面
2. ✅ 查看Actions是否在运行
3. ✅ 等待Windows EXE打包完成
4. ✅ 下载并测试EXE
5. ✅ 分享给需要的人

---

## 💡 快速命令参考

```bash
# 查看状态
git status

# 拉取最新代码
git pull origin main

# 提交修改
git add .
git commit -m "更新说明"
git push origin main

# 查看提交历史
git log --oneline

# 查看远程仓库
git remote -v
```

---

**恭喜！你的项目已成功托管在GitHub上！** 🎊🚀

**仓库地址**：https://github.com/six8888-cpu/bsclianghao

