@echo off
echo ------��ʼ���----------
Pyinstaller -F web.py
echo ------�ƶ��ļ�----------
move .\dist\web.exe .\
rd /s/q build
rd /s/q dist
del /s /Q web.spec
pause
pause