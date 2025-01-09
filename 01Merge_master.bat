@echo off

REM 检查是否有参数传递 --prefix
git subtree merge --prefix=boostregex master
git subtree merge --prefix=PowerEditor master
pause