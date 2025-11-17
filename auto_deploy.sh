#!/bin/bash
# BSC靓号生成器 - 自动部署脚本
# 自动安装所有依赖并配置环境

echo "============================================================"
echo "  BSC靓号生成器 - 自动部署脚本"
echo "============================================================"
echo ""

# 检查是否为root用户
if [ "$EUID" -ne 0 ]; then 
    echo "⚠️  建议使用root用户运行，或使用 sudo ./auto_deploy.sh"
    echo ""
fi

echo "【步骤1/5】更新系统..."
apt update -y
echo "✓ 系统更新完成"
echo ""

echo "【步骤2/5】安装Python3和pip..."
apt install python3 python3-pip -y
echo "✓ Python3安装完成"
python3 --version
echo ""

echo "【步骤3/5】安装screen（后台运行工具）..."
apt install screen -y
echo "✓ Screen安装完成"
echo ""

echo "【步骤4/5】安装Python依赖..."
echo "正在安装 eth-keys, eth-utils, pycryptodome..."
pip3 install eth-keys eth-utils pycryptodome -i https://mirrors.aliyun.com/pypi/simple/
echo "✓ Python依赖安装完成"
echo ""

echo "【步骤5/5】验证环境..."
python3 -c "import eth_keys; import eth_utils; from Crypto.Hash import keccak; print('✓ 所有依赖导入成功')"
echo ""

echo "============================================================"
echo "  部署完成！"
echo "============================================================"
echo ""
echo "📝 使用说明："
echo ""
echo "1. 运行标准版生成器："
echo "   python3 vanity_wallet_generator.py"
echo ""
echo "2. 运行极速版生成器（推荐）："
echo "   python3 fast_generator.py"
echo ""
echo "3. 运行超级靓号生成器（前缀+后缀）："
echo "   python3 ultra_generator.py"
echo ""
echo "4. 后台运行（推荐）："
echo "   screen -S vanity"
echo "   python3 fast_generator.py"
echo "   # 按 Ctrl+A, D 分离"
echo ""
echo "5. 重新连接查看进度："
echo "   screen -r vanity"
echo ""
echo "============================================================"
echo ""
echo "🎉 现在可以开始生成靓号了！"
echo ""



