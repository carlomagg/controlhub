#!/usr/bin/env python
"""
Generate downloadable agent package for the dashboard
This creates client_agent.zip in the static folder
"""

import os
import shutil
import zipfile

def generate_agent_package():
    """Generate agent package for download"""
    
    print("=" * 60)
    print("Generating Downloadable Agent Package")
    print("=" * 60)
    print()
    
    # Ensure static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Create ZIP file directly
    zip_path = 'static/client_agent.zip'
    
    print("Creating client_agent.zip...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add agent files
        files_to_include = [
            ('client_agent/agent.py', 'client_agent/agent.py'),
            ('client_agent/requirements.txt', 'client_agent/requirements.txt'),
            ('client_agent/EASY_INSTALL.bat', 'client_agent/EASY_INSTALL.bat'),
            ('client_agent/START_AGENT.bat', 'client_agent/START_AGENT.bat'),
            ('client_agent/SIMPLE_SETUP_GUIDE.txt', 'client_agent/SIMPLE_SETUP_GUIDE.txt'),
        ]
        
        for source, archive_name in files_to_include:
            if os.path.exists(source):
                zipf.write(source, archive_name)
                print(f"  ✓ Added: {archive_name}")
        
        # Create template config
        config_template = """{
    "server_url": "PASTE_SERVER_URL_HERE",
    "device_token": "PASTE_TOKEN_HERE",
    "device_name": "My Computer",
    "capture_interval": 0.5,
    "jpeg_quality": 60,
    "screen_width": 1280,
    "reconnect_delay": 5
}"""
        zipf.writestr('client_agent/agent_config.json', config_template)
        print(f"  ✓ Added: client_agent/agent_config.json (template)")
    
    file_size = os.path.getsize(zip_path) / 1024  # KB
    
    print()
    print("=" * 60)
    print("✅ Agent package created successfully!")
    print(f"📦 File: {zip_path}")
    print(f"📊 Size: {file_size:.1f} KB")
    print()
    print("The agent is now available for download from the dashboard!")
    print("Users can download it when they create a new device.")
    print("=" * 60)

if __name__ == "__main__":
    generate_agent_package()
