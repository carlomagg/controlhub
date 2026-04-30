@echo off
cls
echo.
echo ============================================================
echo    ControlHub Live Agent - Easy Installation
echo ============================================================
echo.
echo This will set up the monitoring agent on this computer.
echo.
echo What you need:
echo  - Device Token (get from administrator)
echo  - Server URL (get from administrator)
echo.
echo ============================================================
echo.
pause

echo.
echo [Step 1/3] Installing required packages...
echo.
pip install websocket-client==1.9.0 mss==10.2.0 pillow==12.2.0 requests==2.33.1 psutil==6.1.1

echo.
echo ============================================================
echo [Step 2/3] Configuration
echo ============================================================
echo.
echo Opening configuration file...
echo.
echo Please:
echo  1. Replace PASTE_TOKEN_HERE with your device token
echo  2. Replace PASTE_SERVER_URL_HERE with your server URL
echo  3. Save the file (Ctrl+S)
echo  4. Close Notepad
echo.
pause

notepad agent_config.json

echo.
echo ============================================================
echo [Step 3/3] Installation Complete!
echo ============================================================
echo.
echo To start monitoring:
echo  - Double-click START_AGENT.bat
echo.
echo To stop monitoring:
echo  - Close the black window
echo.
echo ============================================================
echo.
pause
