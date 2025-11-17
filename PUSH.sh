#!/bin/bash
# 快速推送到GitHub

echo "🚀 推送到 GitHub..."
echo ""

cd /Users/xiaowu/tst

# 推送
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "访问：https://github.com/six8888-cpu/bsclianghao"
    echo ""
    echo "查看 Actions 自动打包 Windows EXE："
    echo "https://github.com/six8888-cpu/bsclianghao/actions"
    echo ""
else
    echo ""
    echo "❌ 推送失败，可能需要认证"
    echo ""
    echo "请手动执行："
    echo "cd /Users/xiaowu/tst"
    echo "git push -u origin main"
    echo ""
fi

