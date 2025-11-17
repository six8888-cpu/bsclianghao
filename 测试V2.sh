#!/bin/bash
# 测试V2版本新功能

echo "========================================"
echo "  BSC靓号生成器 V2 - 快速测试"
echo "========================================"
echo ""

echo "V2版本新功能："
echo "  ✅ 实时概率显示"
echo "  ✅ 彩色界面输出"
echo "  ✅ 运气状态提示"
echo "  ✅ 详细统计信息"
echo ""

echo "========================================"
echo "  测试命令选项"
echo "========================================"
echo ""
echo "1. 快速测试（3位，几秒完成）"
echo "2. 中等测试（5位，10-30秒）"
echo "3. 实战测试（6位，1-3分钟）"
echo ""

read -p "选择测试 (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "运行：生成后缀888的地址（3位）"
        echo "预计：几秒钟"
        echo ""
        echo -e "888\n\nn\n1\n8\ny" | python3 ultra_generator_v2.py
        ;;
    2)
        echo ""
        echo "运行：生成前缀88888的地址（5位）"
        echo "预计：10-30秒"
        echo ""
        echo -e "88888\n\nn\n1\n8\ny" | python3 ultra_generator_v2.py
        ;;
    3)
        echo ""
        echo "运行：生成前缀+后缀 3a...d32 的地址（5位）"
        echo "预计：1-3分钟"
        echo ""
        echo -e "3a\nd32\nn\n1\n8\ny" | python3 ultra_generator_v2.py
        ;;
    *)
        echo "无效选择"
        exit 1
        ;;
esac

echo ""
echo "========================================"
echo "  测试完成！"
echo "========================================"
echo ""
echo "如果看到："
echo "  ✅ 彩色输出"
echo "  ✅ 概率显示"
echo "  ✅ 运气提示"
echo "  ✅ 详细统计"
echo ""
echo "说明V2版本工作正常！"
echo ""
echo "========================================"

