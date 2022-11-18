@echo off
echo ------开始打包----------
Pyinstaller -F web.py
echo ------移动文件----------
move .\dist\web.exe .\
rd /s/q build
rd /s/q dist
del /s /Q web.spec
pause
pause