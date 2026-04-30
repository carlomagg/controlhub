# ControlHub Live - Complete Guide

**Professional Remote Monitoring & Management Platform**

Everything you need to know in one place.

---

## 📑 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [First Time Setup](#first-time-setup)
4. [Using the Dashboard](#using-the-dashboard)
5. [Adding Devices](#adding-devices)
6. [Configuring the Agent](#configuring-the-agent)
7. [Viewing Live Screens](#viewing-live-screens)
8. [Deploying to Multiple Computers](#deploying-to-multiple-computers)
9. [Working Over Internet](#working-over-internet)
10. [User Management](#user-management)
11. [Troubleshooting](#troubleshooting)
12. [Quick Reference](#quick-reference)

---

## 🚀 Quick Start

### Already Set Up? Jump Here:

**Start Server:**
```cmd
start_server.bat
```

**Start Agent:**
```cmd
cd client_agent
START_AGENT.bat
```

**Access Dashboard:**
```
http://localhost:8000
Login: carlomagg / School67@
```

---

## 📦 Installation

### Step 1: Run Setup

**Windows:**
```cmd
setup.bat
```

**Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Create virtual environment
- Install all dependencies
- Create database
- Prompt you to create admin user

### Step 2: Create Admin Account

When prompted:
- **Username:** carlomagg
- **Email:** rule4real67@gmail.com
- **Password:** School67@

### Step 3: Set Role to Super Admin

```cmd
venv\Scripts\python.exe manage.py shell -c "from accounts.models import User; user = User.objects.get(username='carlomagg'); user.role = 'super_admin'; user.save(); print('Role set to Super Admin')"
```

Or simply run:
```cmd
UNLOCK_ADMIN_DASHBOARD.bat
```

---

## 🎬 First Time Setup

### 1. Start the Server

```cmd
start_server.bat
```

Keep this window open! You should see:
```
Listening on TCP address 0.0.0.0:8000
```

### 2. Access Dashboard

Open browser: `http://localhost:8000`

Login with your credentials.

### 3. You Should See

- **Admin Dashboard** with full features
- **Quick Actions** buttons
- **Full device table**
- **Full user table**
- **System information panel**

If you see a basic dashboard, run `UNLOCK_ADMIN_DASHBOARD.bat` and restart server.

---

## 🖥️ Using the Dashboard

### Main Features:

**Dashboard Home:**
- Total devices, online/offline counts
- Quick action buttons
- Full device management table
- Full user management table
- Recent messages
- System information

**Devices Page:**
- View all devices
- Add new devices
- Monitor live screens
- Send messages
- Delete devices

**Users Page (Super Admin only):**
- View all users
- Create new users
- Edit user roles
- Delete users

**Live Monitor Page:**
- Real-time screen streaming
- Send instant messages
- View device information
- Fullscreen mode

---

## 📱 Adding Devices

### Step 1: Create Device in Dashboard

1. Click **"Devices"** in sidebar
2. Click **"Add Device"** button
3. Fill in:
   - **Device Name:** "Office PC" (any name you want)
   - **Operating System:** Windows/Linux/macOS
4. Click **"Create Device"**
5. You'll see a **complete setup guide** with:
   - Download button for the agent
   - Your device token (automatically shown)
   - Step-by-step instructions
   - Copy-paste ready configuration

### Step 2: Follow the On-Screen Instructions

After creating a device, you'll see a **beautiful setup guide** with:

- **Big "Download Agent" button** - One click to get everything
- **Your token displayed** - With a "Copy" button
- **Step-by-step visual guide** - Numbered steps with icons
- **Automatic configuration** - Server URL already filled in

**It's so easy, anyone can do it!** No technical knowledge needed.

---

## 🤖 Configuring the Agent

### For Your Own Computer (Testing):

**⚠️ Note:** This is ONLY for testing on the same computer as the server!

**Step 1:** Open config file
```cmd
cd client_agent
notepad agent_config.json
```

**Step 2:** Edit configuration
```json
{
    "server_url": "ws://localhost:8000",
    "device_token": "PASTE_YOUR_TOKEN_HERE",
    "device_name": "My Computer"
}
```

**Step 3:** Save (Ctrl+S) and close

**Step 4:** Start agent
```cmd
START_AGENT.bat
```

You should see:
```
WebSocket connected successfully!
Screen capture loop started
```

### For Other Computers (Same Network):

**Step 1:** Find your server IP
```cmd
ipconfig
```
Look for **IPv4 Address** (e.g., 192.168.1.100)

**Step 2:** Edit config on other computer
```json
{
    "server_url": "ws://192.168.1.100:8000",
    "device_token": "PASTE_TOKEN_HERE",
    "device_name": "Office PC"
}
```

**⚠️ IMPORTANT:** Do NOT use `ws://localhost:8000` on other computers! 
That only works on the server computer itself. Always use the actual 
server IP address (e.g., ws://192.168.1.100:8000) or your company's 
hosted URL (e.g., wss://controlhub.yourcompany.com).

**Step 3:** Start agent on that computer

---

## 👁️ Viewing Live Screens

### Step 1: Check Device is Online

1. Go to **Devices** page
2. Look for green **"Online"** badge 🟢

### Step 2: Click Monitor

Click the blue **"Monitor"** button (eye icon 👁️)

### Step 3: View Screen

Wait 2-3 seconds - you'll see the live screen!

### Features While Monitoring:

- **Live screen updates** (2 times per second)
- **Send messages** (right panel)
- **View device info** (CPU, RAM, IP, etc.)
- **Fullscreen mode** (button in corner)
- **Message history**

### Sending Messages:

1. Type message in the box
2. Click **"Send"**
3. Popup appears on the device!

---

## 🌐 Deploying to Multiple Computers

### For Non-Technical Users (Super Easy!):

**What You Do:**

1. Create device in dashboard
2. Click **"Download Agent"** button on the device page
3. Send the ZIP file to the user (email, USB, network share)
4. Send them the token (shown on the device page)

**What User Does:**

1. Extract the ZIP file to Desktop
2. Double-click `EASY_INSTALL.bat`
3. When Notepad opens, paste the token you gave them
4. Save and close Notepad
5. Double-click `START_AGENT.bat`
6. Done! ✅

**That's it!** The device will show as "Online" in your dashboard within 5 seconds.

### Simple User Instructions:

```
1. Extract the client_agent folder
2. Double-click START_AGENT.bat
3. Keep the window open
4. You're now being monitored!

To stop: Close the black window
```

---

## 🌍 Working Over Internet

### Option 1: Local Network Only

**Server URL:** `ws://192.168.1.100:8000`

**Use when:**
- All computers on same WiFi/LAN
- Office network
- Home network

**Setup:**
1. Find server IP: `ipconfig`
2. Use that IP in agent config
3. Done!

### Option 2: Over Internet (Your Computer)

**Server URL:** `ws://YOUR_PUBLIC_IP:8000`

**Steps:**

1. **Find public IP:**
   - Visit: https://whatismyipaddress.com/

2. **Configure port forwarding on router:**
   - Forward port 8000 to your computer's local IP
   - Example: External 8000 → Internal 192.168.1.100:8000

3. **Configure firewall:**
   ```cmd
   netsh advfirewall firewall add rule name="ControlHub" dir=in action=allow protocol=TCP localport=8000
   ```

4. **Use public IP in agent config:**
   ```json
   {
       "server_url": "ws://203.0.113.45:8000"
   }
   ```

### Option 3: VPS/Cloud Server (Professional)

**Server URL:** `wss://controlhub.yourcompany.com`

**Providers:**
- DigitalOcean ($5/month)
- AWS Lightsail ($3.50/month)
- Vultr ($2.50/month)

**Benefits:**
- Always online
- Professional domain
- SSL/HTTPS security
- Better performance

See production deployment section for details.

---

## 👥 User Management

### User Roles:

| Role | View Streams | Send Messages | Manage Devices | Manage Users |
|------|:------------:|:-------------:|:--------------:|:------------:|
| **Viewer** | ✅ | ❌ | ❌ | ❌ |
| **Admin** | ✅ | ✅ | ✅ | ❌ |
| **Super Admin** | ✅ | ✅ | ✅ | ✅ |

### Creating Users:

1. Click **"Users"** in sidebar (Super Admin only)
2. Click **"Add User"**
3. Fill in:
   - Username
   - Email (optional)
   - Password
   - Role
4. Click **"Create User"**

### Editing Users:

1. Go to Users page
2. Click edit icon (pencil)
3. Change role or status
4. Click **"Save Changes"**

---

## 🔧 Troubleshooting

### Server Won't Start

**Problem:** Error when running `start_server.bat`

**Solutions:**
- Check if port 8000 is already in use: `netstat -an | findstr :8000`
- Make sure virtual environment is activated
- Check for error messages in console

### Agent Won't Connect

**Problem:** "Connection refused" or "Invalid token"

**Solutions:**
- Make sure server is running
- Check `server_url` in config is correct
- Verify device token is correct (no extra spaces)
- Check firewall settings

### Device Shows Offline

**Problem:** Device appears with red badge in dashboard

**Solutions:**
- Make sure agent is running (check Command Prompt window)
- Look for "WebSocket connected successfully!" message
- Restart the agent
- Check network connection

### Can't Send Messages

**Problem:** "Permission denied" when trying to send messages

**Solutions:**
- Run `UNLOCK_ADMIN_DASHBOARD.bat`
- Restart server
- Logout and login again
- Check your role is Admin or Super Admin

### No Screen Visible

**Problem:** Monitor page shows "Waiting for stream..."

**Solutions:**
- Wait 5-10 seconds (it takes a moment to start)
- Check agent is running and connected
- Refresh the browser page
- Check agent logs: `client_agent/agent.log`
- Restart the agent

### High CPU Usage

**Problem:** Computer is slow, high CPU usage

**Solutions:**
Edit `agent_config.json`:
```json
{
    "capture_interval": 1.0,
    "jpeg_quality": 40,
    "screen_width": 800
}
```

### Python Not Found

**Problem:** "Python is not recognized"

**Solutions:**
- Install Python from python.org
- Make sure to check "Add Python to PATH" during installation
- Restart Command Prompt after installation

---

## ⚡ Quick Reference

### Common Commands:

**Start Server:**
```cmd
start_server.bat
```

**Start Agent:**
```cmd
cd client_agent
START_AGENT.bat
```

**Fix Permissions:**
```cmd
UNLOCK_ADMIN_DASHBOARD.bat
```

**Find Server IP:**
```cmd
ipconfig
```

**Check User Role:**
```cmd
venv\Scripts\python.exe check_user_role.py
```

### URLs:

- **Dashboard:** `http://localhost:8000`
- **Django Admin:** `http://localhost:8000/admin`
- **Devices:** `http://localhost:8000/devices/`
- **Users:** `http://localhost:8000/accounts/users/`

### Configuration Files:

- **Server:** `controlhub/settings.py`
- **Agent:** `client_agent/agent_config.json`

### Log Files:

- **Agent:** `client_agent/agent.log`
- **Server:** Console output

### Default Credentials:

- **Username:** carlomagg
- **Password:** School67@
- **Role:** Super Admin

---

## 📊 Configuration Options

### Agent Config (`agent_config.json`):

```json
{
    "server_url": "ws://localhost:8000",
    "device_token": "your-token-here",
    "device_name": "My Computer",
    "capture_interval": 0.5,
    "jpeg_quality": 60,
    "screen_width": 1280,
    "reconnect_delay": 5
}
```

**Options Explained:**

- **server_url:** Where your server is running
  - **Localhost (testing only):** `ws://localhost:8000` - Only use this on the same computer as the server
  - **Local network:** `ws://192.168.1.100:8000` - Use the server's actual IP address
  - **Internet:** `ws://YOUR_PUBLIC_IP:8000` - Use your public IP or domain
  - **Company domain:** `wss://controlhub.yourcompany.com` - Use your hosted URL
  
  **⚠️ Common Mistake:** Don't use localhost when deploying to other computers!

- **device_token:** Unique token from dashboard (required)

- **device_name:** Friendly name for this device

- **capture_interval:** Seconds between captures
  - Lower = More real-time, higher CPU (0.2-0.5)
  - Higher = Less CPU, slower updates (1.0-2.0)

- **jpeg_quality:** Image quality 1-100
  - Higher = Better quality, larger files (70-80)
  - Lower = Lower quality, smaller files (40-50)

- **screen_width:** Max screen width in pixels
  - Full HD: 1920
  - HD: 1280
  - Low bandwidth: 800

### Performance Presets:

**High Quality:**
```json
{
    "capture_interval": 0.3,
    "jpeg_quality": 75,
    "screen_width": 1920
}
```

**Balanced (Recommended):**
```json
{
    "capture_interval": 0.5,
    "jpeg_quality": 60,
    "screen_width": 1280
}
```

**Low Bandwidth:**
```json
{
    "capture_interval": 1.0,
    "jpeg_quality": 40,
    "screen_width": 800
}
```

---

## 🔐 Security

### Best Practices:

1. **Use strong passwords** for dashboard
2. **Keep tokens secure** - don't share publicly
3. **Use HTTPS/WSS in production** (not HTTP/WS)
4. **Inform users** they're being monitored
5. **Limit Super Admin access** to trusted personnel
6. **Regular updates** - keep system updated
7. **Firewall rules** - only expose necessary ports

### Changing Passwords:

**Via Django Admin:**
1. Go to `http://localhost:8000/admin`
2. Click Users
3. Select user
4. Click "this form" next to password
5. Enter new password
6. Click "Change Password"

---

## 📱 Mobile Access

### Accessing from Phone/Tablet:

1. **Find server IP:** `ipconfig` on server computer
2. **On mobile browser:** `http://192.168.1.100:8000`
3. **Login** with your credentials
4. **Tap ☰ menu** (top-left) to open sidebar
5. **Navigate** to Devices
6. **Tap Monitor** to view screens

**Tip:** Use landscape mode for better view!

---

## 🎯 Use Cases

- **IT Support** - Remote troubleshooting
- **System Administration** - Monitor servers
- **Remote Work** - Supervise remote workers
- **Education** - Monitor student computers
- **Security** - Surveillance and monitoring
- **DevOps** - Monitor development environments

---

## ✅ Success Checklist

### Server Setup:
- [ ] Ran setup.bat
- [ ] Created admin user
- [ ] Fixed permissions (UNLOCK_ADMIN_DASHBOARD.bat)
- [ ] Server is running
- [ ] Can access dashboard
- [ ] See admin dashboard (not basic)

### Agent Setup:
- [ ] Created device in dashboard
- [ ] Copied device token
- [ ] Edited agent_config.json
- [ ] Pasted token
- [ ] Set correct server URL
- [ ] Started agent
- [ ] Saw "WebSocket connected successfully!"
- [ ] Device shows Online (green badge)

### Monitoring:
- [ ] Can see device in dashboard
- [ ] Device has green "Online" badge
- [ ] Can click "Monitor" button
- [ ] Can see live screen
- [ ] Can send messages
- [ ] Popup appears on device

---

## 🆘 Getting Help

### Check These First:
1. This guide (you're reading it!)
2. Troubleshooting section above
3. Agent logs: `client_agent/agent.log`
4. Server console output

### Common Issues:
- **Permission denied** → Run `UNLOCK_ADMIN_DASHBOARD.bat`
- **Connection refused** → Check server is running
- **Device offline** → Check agent is running
- **Can't see screen** → Wait 5 seconds, refresh page

---

## 🎓 Learning Path

### Day 1: Get It Working
1. Run setup.bat
2. Start server
3. Create device
4. Start agent on same computer
5. Monitor your own screen
6. Send yourself a test message

### Day 2: Add More Devices
1. Create more devices in dashboard
2. Deploy agent to other computers
3. Test monitoring multiple devices
4. Test messaging

### Day 3: Advanced
1. Set up internet access
2. Create more users with different roles
3. Optimize performance
4. Explore all features

---

## 📞 Support

### Documentation:
- This complete guide
- Django documentation: https://docs.djangoproject.com/
- Django Channels: https://channels.readthedocs.io/

### Logs:
- Agent: `client_agent/agent.log`
- Server: Console output

---

## 🎉 Summary

**You have:**
- ✅ Complete monitoring system
- ✅ Easy setup for users
- ✅ Works over local network
- ✅ Works over internet
- ✅ Professional dashboard
- ✅ Role-based access control

**To get started:**
1. Run `setup.bat`
2. Run `start_server.bat`
3. Create device in dashboard
4. Configure and start agent
5. Monitor screens!

**Everything you need is in this one guide!** 🚀

---

**ControlHub Live - Professional Remote Monitoring Made Simple**

*Version 1.0 - Complete Guide*
