#!/bin/bash

# BSC靓号生成器 - 快速启动脚本

echo "========================================"
echo "  BSC靓号生成器"
echo "========================================"
echo ""
echo "请选择版本："
echo ""
echo "  [1] V2增强版 (推荐)"
echo "      - 前缀+后缀+包含灵活组合"
echo "      - 实时概率、彩色界面"
echo "      - 运气评估、详细统计"
echo ""
echo "  [2] 简化版"
echo "      - 单一模式匹配"
echo "      - 适合简单需求"
echo ""
read -p "请输入选择 [1/2]: " choice

case $choice in
    1)
        echo ""
        echo "启动V2增强版..."
        python3 ultra_generator_v2.py
        ;;
    2)
        echo ""
        echo "启动简化版..."
        python3 fast_generator.py
        ;;
    *)
        echo ""
        echo "无效选择，启动V2增强版..."
        python3 ultra_generator_v2.py
        ;;
esac
