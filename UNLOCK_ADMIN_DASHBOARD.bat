@echo off
cls
echo.
echo ============================================================
echo    UNLOCK ADMIN DASHBOARD - ControlHub Live
echo ============================================================
echo.
echo This will:
echo  1. Check your user role
echo  2. Fix it to Super Admin if needed
echo  3. Show you what to do next
echo.
echo ============================================================
echo.

echo [Step 1/3] Checking user role...
echo.
venv\Scripts\python.exe check_user_role.py

echo.
echo ============================================================
echo [Step 2/3] What to do next:
echo ============================================================
echo.
echo 1. STOP the server (Ctrl+C in the server window)
echo 2. START the server again: start_server.bat
echo 3. CLEAR browser cache: Ctrl+Shift+Delete
echo 4. LOGIN again at: http://localhost:8000
echo.
echo You should now see the RICH ADMIN DASHBOARD with:
echo  - Full devices table
echo  - Full users table  
echo  - Quick action buttons
echo  - System info panel
echo  - Admin links panel
echo.
echo ============================================================
echo [Step 3/3] Verification
echo ============================================================
echo.
echo After restarting, you should see:
echo  [x] "Admin Dashboard" title (not just "Dashboard")
echo  [x] "Super Admin" badge in top right
echo  [x] "Quick Actions" section with 4 big buttons
echo  [x] Full table of ALL devices (not just 5)
echo  [x] Full table of ALL users
echo  [x] Monitor/Edit/Delete buttons in tables
echo.
echo If you see all of these - SUCCESS! You have the admin dashboard!
echo.
echo ============================================================
echo.
pause
