#!/bin/bash
# BSC靓号生成器 - 192核服务器一键部署

SERVER_IP="你的服务器IP"
SERVER_USER="root"
SERVER_PASSWORD="你的密码"

echo "============================================================"
echo "  BSC靓号生成器 - 192核超级服务器一键部署"
echo "============================================================"
echo ""
echo "服务器信息："
echo "  IP: $SERVER_IP"
echo "  用户: $SERVER_USER"
echo "  配置: 192核 384GB"
echo ""
echo "============================================================"
echo ""

# 检查是否安装了sshpass
if ! command -v sshpass &> /dev/null; then
    echo "⚠️  需要安装sshpass才能自动输入密码"
    echo ""
    echo "正在尝试安装sshpass..."
    brew install hudochenkov/sshpass/sshpass 2>/dev/null || {
        echo ""
        echo "❌ 自动安装失败"
        echo ""
        echo "请手动安装："
        echo "  brew install hudochenkov/sshpass/sshpass"
        echo ""
        echo "或者手动部署："
        echo "----------------------------------------"
        echo "cd /Users/xiaowu/tst"
        echo "scp *.py requirements.txt auto_deploy.sh root@你的服务器IP:~/"
        echo "ssh root@你的服务器IP"
        echo "chmod +x auto_deploy.sh && ./auto_deploy.sh"
        echo "----------------------------------------"
        exit 1
    }
    echo "✓ sshpass安装成功"
    echo ""
fi

echo "【步骤1/3】上传文件到192核服务器..."
echo "------------------------------------------------"
cd /Users/xiaowu/tst

sshpass -p "$SERVER_PASSWORD" scp -o StrictHostKeyChecking=no \
    fast_generator.py \
    ultra_generator.py \
    requirements.txt \
    auto_deploy.sh \
    $SERVER_USER@$SERVER_IP:~/ || {
    echo "❌ 文件上传失败"
    echo ""
    echo "请检查："
    echo "  1. 服务器IP是否正确: $SERVER_IP"
    echo "  2. 密码是否正确"
    echo "  3. 服务器是否可以连接"
    echo ""
    echo "手动上传命令："
    echo "  scp *.py requirements.txt auto_deploy.sh root@$SERVER_IP:~/"
    exit 1
}
echo "✓ 文件上传成功"
echo ""

echo "【步骤2/3】设置执行权限..."
echo "------------------------------------------------"
sshpass -p "$SERVER_PASSWORD" ssh -o StrictHostKeyChecking=no \
    $SERVER_USER@$SERVER_IP "chmod +x ~/auto_deploy.sh" || {
    echo "❌ 权限设置失败"
    exit 1
}
echo "✓ 权限设置成功"
echo ""

echo "【步骤3/3】在服务器上部署环境..."
echo "------------------------------------------------"
echo "这需要2-5分钟，请稍候..."
echo ""
sshpass -p "$SERVER_PASSWORD" ssh -o StrictHostKeyChecking=no \
    $SERVER_USER@$SERVER_IP "~/auto_deploy.sh" || {
    echo "❌ 环境部署失败"
    echo ""
    echo "请手动连接服务器检查："
    echo "  ssh root@$SERVER_IP"
    exit 1
}

echo ""
echo "============================================================"
echo "  ✅ 部署完成！"
echo "============================================================"
echo ""
echo "验证192核配置..."
CORES=$(sshpass -p "$SERVER_PASSWORD" ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP "nproc")
echo "✓ 服务器CPU核心数: $CORES"
echo ""

if [ "$CORES" != "192" ]; then
    echo "⚠️  警告：实际核心数($CORES)与预期(192)不符"
    echo "   建议将进程数设置为: $CORES"
    echo ""
fi

echo "============================================================"
echo "  🚀 现在可以开始生成靓号了！"
echo "============================================================"
echo ""
echo "【下一步操作】"
echo ""
echo "1. 连接到服务器："
echo "   ssh root@$SERVER_IP"
echo "   密码: $SERVER_PASSWORD"
echo ""
echo "2. 创建screen会话："
echo "   screen -S vanity"
echo ""
echo "3. 运行192核超级生成器（生成 c946...0bb7）："
echo "   echo -e \"c946\\n0bb7\\nn\\n1\\n$CORES\\ny\" | python3 ultra_generator.py"
echo ""
echo "4. 分离会话（让程序后台运行）："
echo "   按 Ctrl+A, 然后按 D"
echo ""
echo "5. 退出服务器："
echo "   exit"
echo ""
echo "============================================================"
echo ""
echo "📊 预期性能："
echo "   速度: 25-35万次/秒"
echo "   耗时: 2-3小时"
echo "   地址: 0xc946...0bb7"
echo ""
echo "📝 查看进度："
echo "   ssh root@$SERVER_IP"
echo "   screen -r vanity"
echo ""
echo "💾 下载结果："
echo "   scp root@$SERVER_IP:~/ultra_vanity_wallets.txt ./"
echo ""
echo "============================================================"

