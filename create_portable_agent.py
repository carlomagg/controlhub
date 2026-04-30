#!/usr/bin/env python
"""
Create a portable agent package for easy distribution
This creates a simple package that non-technical users can use
"""

import os
import shutil
import zipfile

def create_portable_agent():
    """Create portable agent package"""
    
    print("Creating Portable Agent Package...")
    print("=" * 60)
    
    # Create portable directory
    portable_dir = "ControlHub-Agent-Portable"
    if os.path.exists(portable_dir):
        shutil.rmtree(portable_dir)
    os.makedirs(portable_dir)
    
    # Copy agent files
    print("Copying agent files...")
    shutil.copy("client_agent/agent.py", f"{portable_dir}/agent.py")
    shutil.copy("client_agent/requirements.txt", f"{portable_dir}/requirements.txt")
    
    # Create simple config template
    config_template = """{
    "server_url": "PASTE_SERVER_URL_HERE",
    "device_token": "PASTE_TOKEN_HERE",
    "device_name": "My Computer",
    "capture_interval": 0.5,
    "jpeg_quality": 60,
    "screen_width": 1280,
    "reconnect_delay": 5
}"""
    
    with open(f"{portable_dir}/agent_config.json", "w") as f:
        f.write(config_template)
    
    # Create simple setup script
    setup_script = """@echo off
echo ============================================================
echo ControlHub Live Agent - Easy Setup
echo ============================================================
echo.
echo This will install the monitoring agent on your computer.
echo.
pause

echo Installing Python packages...
pip install websocket-client==1.9.0 mss==10.2.0 pillow==12.2.0 requests==2.33.1 psutil==6.1.1

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit agent_config.json (right-click, Open with Notepad)
echo 2. Paste your device token
echo 3. Paste your server URL
echo 4. Save the file
echo 5. Run START_AGENT.bat
echo.
pause
"""
    
    with open(f"{portable_dir}/SETUP.bat", "w") as f:
        f.write(setup_script)
    
    # Create start script
    start_script = """@echo off
echo ============================================================
echo ControlHub Live Agent
echo ============================================================
echo.
echo Starting monitoring agent...
echo Keep this window open!
echo.
python agent.py
pause
"""
    
    with open(f"{portable_dir}/START_AGENT.bat", "w") as f:
        f.write(start_script)
    
    # Create README
    readme = """# ControlHub Live Agent - Simple Setup Guide

## For Non-Technical Users

### What This Does
This agent allows your computer to be monitored remotely through ControlHub Live.

### Requirements
- Windows computer
- Python installed (download from python.org if needed)
- Internet connection
- Device token from your administrator

### Step 1: Get Your Device Token
Ask your administrator for:
1. Device Token (long code)
2. Server URL (web address)

### Step 2: Run Setup
1. Double-click SETUP.bat
2. Wait for installation to complete

### Step 3: Configure
1. Right-click agent_config.json
2. Select "Open with Notepad"
3. Replace PASTE_TOKEN_HERE with your actual token
4. Replace PASTE_SERVER_URL_HERE with your server URL
5. Save and close

### Step 4: Start Agent
1. Double-click START_AGENT.bat
2. Keep the window open
3. You're now being monitored!

### To Stop Monitoring
Close the black window (Command Prompt)

### Troubleshooting
- If Python is not installed, download from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Contact your administrator if you have issues

### What Gets Monitored
- Your screen (everything you see)
- You'll receive popup messages from administrators

### Privacy
- Only administrators can view your screen
- The agent must be running for monitoring to work
- You can stop it anytime by closing the window
"""
    
    with open(f"{portable_dir}/README.txt", "w") as f:
        f.write(readme)
    
    # Create ZIP file
    print("Creating ZIP file...")
    zip_filename = "ControlHub-Agent-Portable.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(portable_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(portable_dir))
                zipf.write(file_path, arcname)
    
    print("=" * 60)
    print("✅ Portable agent package created!")
    print(f"📦 Package: {zip_filename}")
    print(f"📁 Folder: {portable_dir}/")
    print()
    print("You can now:")
    print("1. Share the ZIP file with users")
    print("2. They extract it")
    print("3. They run SETUP.bat")
    print("4. They edit config with their token")
    print("5. They run START_AGENT.bat")
    print()
    print("That's it! No technical knowledge needed!")

if __name__ == "__main__":
    create_portable_agent()
