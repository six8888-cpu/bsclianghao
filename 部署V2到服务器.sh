#!/bin/bash
# 快速部署V2版本到服务器

echo "========================================"
echo "  BSC靓号生成器 V2 - 服务器部署"
echo "========================================"
echo ""

# 服务器信息
SERVER_192="你的服务器IP"
SERVER_8="你的服务器IP_2"
USER="root"
PASS_192="你的密码"
PASS_8="你的密码"

echo "选择目标服务器："
echo "  1. 192核服务器 (你的服务器IP)"
echo "  2. 8核服务器 (你的服务器IP_2)"
echo ""

read -p "选择 (1/2): " choice

case $choice in
    1)
        SERVER=$SERVER_192
        PASSWORD=$PASS_192
        CORES=192
        echo ""
        echo "目标：192核服务器 ($SERVER)"
        ;;
    2)
        SERVER=$SERVER_8
        PASSWORD=$PASS_8
        CORES=8
        echo ""
        echo "目标：8核服务器 ($SERVER)"
        ;;
    *)
        echo "无效选择"
        exit 1
        ;;
esac

echo ""
echo "========================================"
echo "  【步骤1/2】上传V2版本到服务器"
echo "========================================"
echo ""

# 上传V2版本
sshpass -p "$PASSWORD" scp -o StrictHostKeyChecking=no \
    ultra_generator_v2.py \
    requirements.txt \
    $USER@$SERVER:~/ || {
    echo "❌ 上传失败"
    echo ""
    echo "请检查："
    echo "  1. 是否安装了sshpass"
    echo "  2. 服务器地址是否正确"
    echo "  3. 网络连接是否正常"
    exit 1
}

echo "✅ V2版本上传成功！"
echo ""

echo "========================================"
echo "  【步骤2/2】部署完成，使用指南"
echo "========================================"
echo ""

echo "🎉 V2版本已上传到服务器！"
echo ""
echo "新功能："
echo "  ✅ 实时概率显示"
echo "  ✅ 彩色界面输出"
echo "  ✅ 运气状态提示"
echo "  ✅ 详细统计信息"
echo ""

echo "========================================"
echo "  快速运行命令"
echo "========================================"
echo ""

echo "1. 连接服务器："
echo "   ssh $USER@$SERVER"
echo ""

echo "2. 快速测试（后缀888，几秒完成）："
echo "   screen -S test"
echo "   echo -e \"888\n\nn\n1\n$CORES\ny\" | python3 ultra_generator_v2.py"
echo "   按 Ctrl+A, D 分离"
echo ""

echo "3. 生成超级靓号（c946...0bb7）："
echo "   screen -S vanity"
echo "   echo -e \"c946\n0bb7\nn\n1\n$CORES\ny\" | python3 ultra_generator_v2.py"
echo "   按 Ctrl+A, D 分离"
echo ""

echo "4. 查看进度："
echo "   screen -r vanity"
echo "   按 Ctrl+A, D 分离"
echo ""

echo "5. 下载结果："
echo "   scp $USER@$SERVER:~/ultra_vanity_wallets.txt ./"
echo ""

echo "========================================"
echo ""
echo "立即体验V2版本的新功能吧！🚀✨"
echo ""
echo "========================================"

