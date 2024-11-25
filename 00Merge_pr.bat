@echo off

REM 检查是否有参数传递
if "%~1"=="" (
    REM 如果没有传递参数，提示用户输入PR编号
    set /p PR_NUMBER=请输入PR编号:
) else (
    REM 如果传递了参数，将参数赋值给PR_NUMBER
    set PR_NUMBER=%1
)


REM 检查是否输入了PR号码
if "%pr_number%"=="" (
    echo 未输入PR号码，请重新运行脚本并提供PR编号。
    exit /b 1
)

REM 检查是否为五位数字
if not "%pr_number%"=="%pr_number:~0,5%" (
    echo 输入的PR号码不是五位数字。
    exit /b 1
)

git remote add upstream https://github.com/notepad-plus-plus/notepad-plus-plus.git

REM 检查命令是否成功执行
if %errorlevel% neq 0 (
	rem 命令执行失败，请检查输入的PR号码是否正确以及网络连接。
	git remote set-url origin https://github.com/notepad-plus-plus/notepad-plus-plus.git
) else (
	echo 命令执行成功。
)

git fetch upstream pull/%pr_number%/head:pr-%pr_number%
git merge pr-%pr_number%


git remote set-url origin https://github.com/indiff/notepad-plus-plus.git

pause