@echo off

REM ����Ƿ��в�������
if "%~1"=="" (
    REM ���û�д��ݲ�������ʾ�û�����PR���
    set /p PR_NUMBER=������PR���:
) else (
    REM ��������˲�������������ֵ��PR_NUMBER
    set PR_NUMBER=%1
)


REM ����Ƿ�������PR����
if "%pr_number%"=="" (
    echo δ����PR���룬���������нű����ṩPR��š�
    exit /b 1
)

REM ����Ƿ�Ϊ��λ����
if not "%pr_number%"=="%pr_number:~0,5%" (
    echo �����PR���벻����λ���֡�
    exit /b 1
)

git remote add upstream https://github.com/notepad-plus-plus/notepad-plus-plus.git

REM ��������Ƿ�ɹ�ִ��
if %errorlevel% neq 0 (
	rem ����ִ��ʧ�ܣ����������PR�����Ƿ���ȷ�Լ��������ӡ�
	git remote set-url origin https://github.com/notepad-plus-plus/notepad-plus-plus.git
) else (
	echo ����ִ�гɹ���
)

git fetch upstream pull/%pr_number%/head:pr-%pr_number%
git merge pr-%pr_number%


git remote set-url origin https://github.com/indiff/notepad-plus-plus.git

pause