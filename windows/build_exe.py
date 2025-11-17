#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BSC靓号生成器 - Windows EXE打包脚本
使用PyInstaller将Python脚本打包为Windows可执行文件
"""

import os
import sys
import subprocess
import shutil

def main():
    print("=" * 70)
    print("BSC靓号生成器 - Windows EXE打包工具")
    print("=" * 70)
    print()
    
    # 检查PyInstaller
    print("【步骤1/4】检查PyInstaller...")
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装")
        print()
        print("正在安装 PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller 安装完成")
    print()
    
    # 清理旧文件
    print("【步骤2/4】清理旧文件...")
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['ultra_generator_windows.spec']
    
    for d in dirs_to_clean:
        if os.path.exists(d):
            shutil.rmtree(d)
            print(f"✓ 已删除: {d}/")
    
    for f in files_to_clean:
        if os.path.exists(f):
            os.remove(f)
            print(f"✓ 已删除: {f}")
    print()
    
    # 打包
    print("【步骤3/4】开始打包...")
    print("这可能需要几分钟，请耐心等待...")
    print()
    
    cmd = [
        'pyinstaller',
        '--onefile',                          # 打包成单个文件
        '--name=BSC-Vanity-Generator',        # 程序名称
        '--icon=NONE',                        # 图标（如果有的话）
        '--console',                          # 保持控制台窗口
        '--clean',                            # 清理临时文件
        '--noconfirm',                        # 不询问覆盖
        '--hidden-import=eth_keys',          # 隐藏导入
        '--hidden-import=eth_utils',
        '--hidden-import=Crypto',
        '--hidden-import=Crypto.Hash',
        '--hidden-import=Crypto.Hash.keccak',
        'ultra_generator_windows.py'
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("✓ 打包成功！")
    except subprocess.CalledProcessError as e:
        print("✗ 打包失败！")
        print(e.stderr)
        return False
    print()
    
    # 验证
    print("【步骤4/4】验证打包结果...")
    exe_path = os.path.join('dist', 'BSC-Vanity-Generator.exe')
    if os.path.exists(exe_path):
        file_size = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"✓ EXE文件已生成")
        print(f"  路径: {exe_path}")
        print(f"  大小: {file_size:.2f} MB")
    else:
        print("✗ 未找到EXE文件")
        return False
    print()
    
    # 完成
    print("=" * 70)
    print("【打包完成】")
    print("=" * 70)
    print()
    print("生成的文件：")
    print(f"  📁 dist/BSC-Vanity-Generator.exe  ({file_size:.2f} MB)")
    print()
    print("下一步：")
    print("  1. 将 dist/BSC-Vanity-Generator.exe 复制到Windows电脑")
    print("  2. 双击运行即可使用")
    print("  3. 无需安装Python环境")
    print()
    print("注意事项：")
    print("  ⚠️  首次运行可能被杀毒软件拦截（添加信任即可）")
    print("  ⚠️  确保Windows电脑有足够的CPU资源")
    print("  ⚠️  生成的钱包文件在EXE同目录下")
    print()
    print("=" * 70)
    
    return True


if __name__ == "__main__":
    success = main()
    
    if not success:
        print()
        print("打包失败，请检查错误信息")
        sys.exit(1)

