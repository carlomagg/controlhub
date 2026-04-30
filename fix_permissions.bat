@echo off
echo ============================================================
echo ControlHub Live - Fix User Permissions
echo ============================================================
echo.

echo Checking and fixing user role for carlomagg...
venv\Scripts\python.exe check_user_role.py

echo.
echo ============================================================
echo Done! Please restart the server and try again.
echo ============================================================
pause
