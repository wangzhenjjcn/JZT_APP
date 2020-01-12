@echo off
chcp 65001
pyinstaller -y -F -w .\app.py  -i ico.ico
pause();
 