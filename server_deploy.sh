#!/bin/bash

# BSC靓号生成器 - 服务器一键部署脚本
# 适用于 Ubuntu / Debian / CentOS / macOS

set -e

echo "========================================"
echo "  BSC靓号生成器 - 服务器一键部署"
echo "========================================"
echo ""

# 检测操作系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    OS=$(uname -s)
fi

echo "检测到系统: $OS"
echo ""

# 1. 安装Python3
echo "【1/5】检查Python3..."
if ! command -v python3 &> /dev/null; then
    echo "Python3未安装，开始安装..."
    case $OS in
        ubuntu|debian)
            sudo apt update
            sudo apt install -y python3 python3-pip
            ;;
        centos|rhel)
            sudo yum install -y python3 python3-pip
            ;;
        darwin)
            echo "macOS请使用: brew install python3"
            exit 1
            ;;
        *)
            echo "未知系统，请手动安装Python3"
            exit 1
            ;;
    esac
else
    echo "✓ Python3已安装: $(python3 --version)"
fi
echo ""

# 2. 安装pip
echo "【2/5】检查pip..."
if ! command -v pip3 &> /dev/null; then
    echo "pip3未安装，开始安装..."
    case $OS in
        ubuntu|debian)
            sudo apt install -y python3-pip
            ;;
        centos|rhel)
            sudo yum install -y python3-pip
            ;;
        *)
            echo "未知系统，请手动安装pip3"
            exit 1
            ;;
    esac
else
    echo "✓ pip3已安装"
fi
echo ""

# 3. 安装screen（可选，用于后台运行）
echo "【3/5】检查screen..."
if ! command -v screen &> /dev/null; then
    echo "screen未安装，开始安装..."
    case $OS in
        ubuntu|debian)
            sudo apt install -y screen 2>/dev/null || echo "⚠ screen安装失败，可使用nohup替代"
            ;;
        centos|rhel)
            # CentOS需要先安装EPEL
            echo "尝试安装EPEL仓库..."
            sudo yum install -y epel-release 2>/dev/null || true
            sudo yum install -y screen 2>/dev/null || echo "⚠ screen安装失败，可使用nohup替代"
            ;;
        *)
            echo "⚠ 跳过screen安装"
            ;;
    esac
    
    # 检查是否安装成功
    if command -v screen &> /dev/null; then
        echo "✓ screen已安装"
    else
        echo "✓ screen未安装（不影响使用，可用nohup后台运行）"
    fi
else
    echo "✓ screen已安装"
fi
echo ""

# 4. 克隆/更新项目
echo "【4/5】获取项目代码..."
if [ -d "bsclianghao" ]; then
    echo "项目已存在，更新中..."
    cd bsclianghao
    git pull
else
    echo "克隆项目..."
    git clone https://github.com/six8888-cpu/bsclianghao.git
    cd bsclianghao
fi
echo "✓ 项目代码已就绪"
echo ""

# 5. 安装Python依赖
echo "【5/5】安装Python依赖..."
pip3 install -r requirements.txt
echo "✓ 依赖安装完成"
echo ""

# 完成
echo "========================================"
echo "  部署完成！"
echo "========================================"
echo ""
echo "🚀 使用方法："
echo ""
echo "方法1：直接运行（前台，可看实时进度）"
echo "   python3 ultra_generator_v2.py"
echo ""
echo "方法2：后台运行 - 使用screen（推荐）"
if command -v screen &> /dev/null; then
    echo "   screen -S bsc"
    echo "   python3 ultra_generator_v2.py"
    echo "   # 按 Ctrl+A 然后 D 退出（程序继续运行）"
    echo "   # 恢复会话: screen -r bsc"
    echo "   # 停止程序: screen -r bsc 然后按 Ctrl+C"
else
    echo "   ⚠ screen未安装，请使用方法3"
fi
echo ""
echo "方法3：后台运行 - 使用nohup"
echo "   nohup python3 ultra_generator_v2.py > output.log 2>&1 &"
echo "   # 查看日志: tail -f output.log"
echo "   # 停止程序: pkill -f ultra_generator"
echo ""
echo "📊 查看CPU核心数："
echo "   nproc"
echo ""
echo "💡 建议进程数 = CPU核心数（程序会自动检测）"
echo ""
echo "========================================"

