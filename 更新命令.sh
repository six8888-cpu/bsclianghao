#!/bin/bash
# 快速更新到服务器

echo "========================================"
echo "  更新优化版本到服务器"
echo "========================================"
echo ""

# 192核服务器
echo "【192核服务器】你的服务器IP"
echo "上传命令："
echo "scp ultra_generator.py fast_generator.py root@你的服务器IP:~/"
echo ""

# 8核服务器
echo "【8核服务器】你的服务器IP_2"
echo "上传命令："
echo "scp ultra_generator.py fast_generator.py root@你的服务器IP_2:~/"
echo ""

echo "========================================"
echo ""

read -p "是否现在上传到192核服务器? (y/n): " choice

if [ "$choice" = "y" ]; then
    echo ""
    echo "正在上传到 你的服务器IP..."
    scp ultra_generator.py fast_generator.py root@你的服务器IP:~/
    echo ""
    echo "✓ 上传完成！"
    echo ""
    echo "运行命令："
    echo "ssh root@你的服务器IP"
    echo "screen -S vanity"
    echo "echo -e \"c946\\n0bb7\\nn\\n1\\n192\\ny\" | python3 ultra_generator.py"
fi

echo ""
echo "========================================"



