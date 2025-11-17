# BSC靓号生成器 - Windows版本

## 📁 本文件夹说明

此文件夹包含所有Windows相关的文件和文档。

---

## 📋 文件列表

### 核心程序
- **`ultra_generator_windows.py`** - Windows专用版本
  - 包含所有V2功能
  - Windows优化（彩色输出、暂停、清屏）
  - 可打包为独立EXE

### 打包工具
- **`build.bat`** - Windows一键打包脚本（推荐）
- **`build_exe.py`** - Python打包脚本（跨平台）

### 文档
- **`Windows版本说明.md`** - 详细使用说明（15000+字）
- **`Windows快速开始.txt`** - 快速参考卡片
- **`打包Windows版本教程.md`** - 打包详细教程

---

## 🚀 快速开始

### 方案1：使用已打包的EXE（最简单）

如果你有打包好的`BSC靓号生成器.exe`：
```bash
# 双击运行即可
BSC靓号生成器.exe
```

### 方案2：自己打包EXE（推荐）

**在Windows电脑上：**

1. 安装Python 3.7+ (https://www.python.org/downloads/)
   - ⚠️ 勾选"Add Python to PATH"

2. 将此文件夹和上级目录的`requirements.txt`复制到Windows

3. 双击运行打包脚本：
   ```cmd
   build.bat
   ```

4. 等待5-10分钟，在`dist`文件夹找到：
   ```
   BSC靓号生成器.exe (约30-50MB)
   ```

### 方案3：使用GitHub Actions自动打包

项目已配置GitHub Actions，push代码后自动打包。

查看：`../.github/workflows/build-windows.yml`

---

## 📊 Windows版本特点

### ✅ 优势
- **无需Python环境** - 双击即用
- **独立可执行文件** - 单个EXE包含一切
- **Windows优化** - 彩色界面、窗口标题
- **所有V2功能** - 概率显示、运气提示
- **便携性强** - 可复制到任何Windows电脑

### 适用场景
- ✅ Windows个人电脑
- ✅ 不想装Python环境
- ✅ 简单到中等靓号（4-8位）
- ✅ 偶尔使用

---

## 📖 详细文档

1. **Windows版本说明.md** - 完整使用指南
   - 使用方法
   - 常见问题
   - 安全建议

2. **Windows快速开始.txt** - 快速参考
   - 一页纸说明
   - 快速测试

3. **打包Windows版本教程.md** - 打包详解
   - Windows打包
   - macOS交叉编译
   - GitHub Actions

---

## ⚠️ 注意事项

### 杀毒软件
- 可能被误报为病毒
- 解决：添加到信任列表或自己打包

### 性能
- EXE首次启动稍慢（解压）
- 生成速度与Python版本完全相同
- 充分利用CPU多核心

### 系统要求
- **最低**: Windows 7 SP1 (64位) + 2核CPU + 2GB内存
- **推荐**: Windows 10/11 (64位) + 8核CPU + 8GB内存

---

## 🆚 Windows vs Linux

| 特性 | Windows EXE | Linux脚本 |
|------|------------|-----------|
| 速度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 便利性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 适用场景 | 个人电脑 | 服务器 |
| 超级靓号 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**建议**：
- 4-7位靓号 → Windows EXE（个人电脑）
- 8-10位靓号 → Linux服务器（高性能）

---

## 🔗 相关链接

- **主项目**: `../`
- **Linux版本**: `../ultra_generator_v2.py`
- **服务器部署**: `../服务器部署指南.md`
- **完整文档**: `../文件说明.md`

---

## 💡 使用流程

```
1. 在Windows电脑上
   ├── 方案A：使用EXE → 双击运行
   └── 方案B：打包EXE → build.bat

2. 配置参数
   ├── 前缀: 如 1780
   ├── 后缀: 如 3CffbD
   └── 进程数: 等于CPU核心数

3. 等待生成
   └── 查看实时进度、概率、速度

4. 获取结果
   └── ultra_vanity_wallets.txt
```

---

## 🎉 开始使用

查看 **`Windows快速开始.txt`** 获取最快速的上手指南！

或查看 **`Windows版本说明.md`** 获取完整说明！

---

**Windows版本让BSC靓号生成更简单！** 🚀💎

