#!/bin/bash
# 推送代码到GitHub

echo "========================================"
echo "  推送BSC靓号生成器到GitHub"
echo "========================================"
echo ""
echo "仓库地址: https://github.com/six8888-cpu/bsclianghao"
echo ""
echo "========================================"
echo ""

cd /Users/xiaowu/tst

echo "【步骤1/2】检查Git状态..."
git status
echo ""

echo "【步骤2/2】推送到GitHub..."
echo ""
echo "正在推送，可能需要输入GitHub用户名和密码/Token..."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "  ✅ 推送成功！"
    echo "========================================"
    echo ""
    echo "下一步："
    echo "1. 访问：https://github.com/six8888-cpu/bsclianghao"
    echo "2. 查看 Actions 标签页"
    echo "3. 等待 GitHub Actions 自动打包 Windows EXE（约5-10分钟）"
    echo "4. 完成后在 Actions 中下载 EXE 文件"
    echo ""
    echo "恭喜！项目已成功上传到GitHub！🎉"
    echo "========================================"
else
    echo ""
    echo "========================================"
    echo "  ❌ 推送失败"
    echo "========================================"
    echo ""
    echo "可能原因："
    echo "1. 需要GitHub认证"
    echo "2. 仓库不存在或没有权限"
    echo ""
    echo "解决方案："
    echo "1. 使用SSH方式（推荐）："
    echo "   git remote set-url origin git@github.com:six8888-cpu/bsclianghao.git"
    echo "   git push -u origin main"
    echo ""
    echo "2. 使用Personal Access Token："
    echo "   访问：https://github.com/settings/tokens"
    echo "   生成Token，然后使用Token作为密码"
    echo ""
    echo "3. 配置GitHub CLI："
    echo "   brew install gh"
    echo "   gh auth login"
    echo "   git push -u origin main"
    echo ""
fi

