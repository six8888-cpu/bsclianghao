#!/bin/bash
# BSC靓号生成器快速启动脚本

echo "=================================="
echo "   BSC靓号生成器"
echo "=================================="
echo ""
echo "请选择版本："
echo "  1. 极速版 (前缀/后缀/包含，单一匹配)"
echo "  2. 超级版 (前缀+后缀，组合匹配)"
echo ""
read -p "请选择 (1/2): " choice

if [ "$choice" = "2" ]; then
    echo ""
    echo "启动超级版..."
    python3 ultra_generator.py
else
    echo ""
    echo "启动极速版..."
    python3 fast_generator.py
fi

