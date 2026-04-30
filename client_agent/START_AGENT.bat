@echo off
cls
echo.
echo ============================================================
echo    ControlHub Live Agent - Starting...
echo ============================================================
echo.
echo Your computer is now being monitored.
echo.
echo IMPORTANT: Keep this window open!
echo Closing this window will stop monitoring.
echo.
echo ============================================================
echo.

python agent.py

echo.
echo ============================================================
echo Agent stopped.
echo ============================================================
echo.
pause
