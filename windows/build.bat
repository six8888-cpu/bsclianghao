@echo off
chcp 65001 >nul
REM BSC靓号生成器 - Windows EXE打包脚本

echo ======================================================================
echo BSC靓号生成器 - Windows EXE 一键打包
echo ======================================================================
echo.

echo 【提示】请确保已安装Python 3.7+和pip
echo.
pause

echo 【步骤1/5】检查Python环境...
python --version
if errorlevel 1 (
    echo ✗ Python未安装或未添加到PATH
    echo.
    echo 请先安装Python: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✓ Python环境正常
echo.

echo 【步骤2/5】安装依赖包...
pip install -r requirements.txt
if errorlevel 1 (
    echo ✗ 依赖安装失败
    pause
    exit /b 1
)
echo ✓ 依赖安装完成
echo.

echo 【步骤3/5】安装PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo ✗ PyInstaller安装失败
    pause
    exit /b 1
)
echo ✓ PyInstaller安装完成
echo.

echo 【步骤4/5】清理旧文件...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist ultra_generator_windows.spec del /f /q ultra_generator_windows.spec
echo ✓ 清理完成
echo.

echo 【步骤5/5】开始打包（需要几分钟）...
pyinstaller --onefile --name=BSC-Vanity-Generator --console --clean --noconfirm --hidden-import=eth_keys --hidden-import=eth_utils --hidden-import=Crypto --hidden-import=Crypto.Hash --hidden-import=Crypto.Hash.keccak ultra_generator_windows.py
if errorlevel 1 (
    echo ✗ 打包失败
    pause
    exit /b 1
)
echo ✓ 打包完成
echo.

echo ======================================================================
echo 【打包成功】
echo ======================================================================
echo.
echo 生成的文件：
echo   📁 dist\BSC靓号生成器.exe
echo.
echo 下一步：
echo   1. 在 dist 文件夹中找到 BSC靓号生成器.exe
echo   2. 双击运行即可使用
echo   3. 可以复制到任何Windows电脑使用
echo.
echo 注意事项：
echo   ⚠️  首次运行可能被杀毒软件拦截（添加信任）
echo   ⚠️  EXE文件大小约30-50MB（包含所有依赖）
echo   ⚠️  生成的钱包文件在EXE同目录下
echo.
echo ======================================================================
echo.

explorer dist
pause

