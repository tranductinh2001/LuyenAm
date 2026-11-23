@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ===============================================================
echo   BIT1 AI ENGLISH VOICE STUDIO - CONG DONG LAP 5180
echo ===============================================================
echo Dang khoi dong server tai http://localhost:5180 ...
start "" http://localhost:5180
python server_luyen_am.py
pause

