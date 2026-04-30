# Server URL Configuration Guide

## Understanding Server URLs

When configuring the ControlHub agent, the **server URL** is the most critical setting. Using the wrong URL is the #1 cause of connection failures.

---

## ⚠️ Common Mistake

**WRONG:** Using `ws://localhost:8000` on remote computers  
**RIGHT:** Using the actual server IP or domain

**Why?** `localhost` means "this computer" - it only works on the server computer itself!

---

## 🎯 Which URL Should I Use?

### Scenario 1: Testing on the Server Computer

**Use:** `ws://localhost:8000`

**When:** You're running the agent on the SAME computer as the server

**Example:**
```json
{
    "server_url": "ws://localhost:8000",
    "device_token": "your-token-here"
}
```

---

### Scenario 2: Same Office/Local Network

**Use:** `ws://SERVER_IP:8000`

**When:** Computers are on the same WiFi or LAN

**How to find server IP:**
```cmd
ipconfig
```
Look for **IPv4 Address** (e.g., 192.168.1.100)

**Example:**
```json
{
    "server_url": "ws://192.168.1.100:8000",
    "device_token": "your-token-here"
}
```

---

### Scenario 3: Over the Internet (Public IP)

**Use:** `ws://YOUR_PUBLIC_IP:8000`

**When:** Monitoring computers outside your network

**How to find public IP:**
- Visit: https://whatismyipaddress.com/

**Example:**
```json
{
    "server_url": "ws://203.0.113.45:8000",
    "device_token": "your-token-here"
}
```

**Requirements:**
- Port forwarding configured on router
- Firewall allows port 8000

---

### Scenario 4: Company Domain (Professional)

**Use:** `wss://controlhub.yourcompany.com`

**When:** Hosted on a VPS/cloud server with SSL

**Example:**
```json
{
    "server_url": "wss://controlhub.yourcompany.com",
    "device_token": "your-token-here"
}
```

**Note:** Uses `wss://` (secure) instead of `ws://`

---

## 📋 Quick Decision Tree

```
Are you testing on the server computer itself?
├─ YES → Use: ws://localhost:8000
└─ NO → Continue...

Are all computers on the same network?
├─ YES → Use: ws://SERVER_IP:8000 (e.g., ws://192.168.1.100:8000)
└─ NO → Continue...

Do you have a company domain with SSL?
├─ YES → Use: wss://controlhub.yourcompany.com
└─ NO → Use: ws://YOUR_PUBLIC_IP:8000
```

---

## 🔍 How to Find Your Server IP

### Windows:
```cmd
ipconfig
```
Look for: **IPv4 Address**

### Linux/macOS:
```bash
ifconfig
# or
ip addr show
```

### Common IP Ranges:
- **192.168.x.x** - Home/office network
- **10.x.x.x** - Corporate network
- **172.16.x.x to 172.31.x.x** - Private network

---

## ✅ Testing Your Configuration

### Step 1: Verify Server is Running
```cmd
start_server.bat
```

### Step 2: Test from Browser
Open: `http://SERVER_IP:8000`

If you can access the dashboard, the URL is correct!

### Step 3: Configure Agent
Use the same IP/domain in the agent config:
- Browser: `http://192.168.1.100:8000`
- Agent: `ws://192.168.1.100:8000`

---

## 🚨 Troubleshooting

### "Connection refused"

**Possible causes:**
1. Wrong server URL
2. Server not running
3. Firewall blocking connection
4. Wrong port number

**Solution:**
- Verify server IP: `ipconfig`
- Test in browser first
- Check firewall settings

### "Invalid token"

**Possible causes:**
1. Token has extra spaces
2. Token is incorrect
3. Token was regenerated

**Solution:**
- Copy token again from dashboard
- Paste carefully (no extra spaces)
- Verify in agent_config.json

### Device shows "Offline"

**Possible causes:**
1. Agent not running
2. Wrong server URL
3. Network issue

**Solution:**
- Check agent window is open
- Verify server URL is correct
- Test network connection

---

## 📝 Configuration Examples

### Example 1: Testing Setup
```json
{
    "server_url": "ws://localhost:8000",
    "device_token": "abc123...",
    "device_name": "Test Computer"
}
```

### Example 2: Office Network
```json
{
    "server_url": "ws://192.168.1.100:8000",
    "device_token": "abc123...",
    "device_name": "Office PC 1"
}
```

### Example 3: Remote Worker
```json
{
    "server_url": "ws://203.0.113.45:8000",
    "device_token": "abc123...",
    "device_name": "Remote Worker - John"
}
```

### Example 4: Professional Deployment
```json
{
    "server_url": "wss://controlhub.acmecorp.com",
    "device_token": "abc123...",
    "device_name": "Sales Dept - PC 5"
}
```

---

## 🎓 Best Practices

1. **Test locally first** - Use localhost on server computer
2. **Document your server URL** - Share it with all users
3. **Use consistent naming** - Help identify devices easily
4. **Keep tokens secure** - Don't share publicly
5. **Use SSL in production** - Switch to wss:// for security

---

## 📞 What to Tell Users

When deploying to users, provide:

1. **The ZIP file** (client_agent.zip)
2. **Their device token** (from dashboard)
3. **The server URL** (NOT localhost!)

**Example message to users:**

```
Hi Team,

Please install the monitoring agent:

1. Extract the attached ZIP file
2. Double-click EASY_INSTALL.bat
3. When Notepad opens, paste this token:
   abc123def456ghi789...

4. Change the server URL to:
   ws://192.168.1.100:8000

5. Save and close Notepad
6. Double-click START_AGENT.bat

Keep the window open!

Questions? Contact IT support.
```

---

## 🔐 Security Notes

- **ws://** = Unencrypted (OK for local network)
- **wss://** = Encrypted (Required for internet)

**For production/internet use:**
- Always use wss:// (secure WebSocket)
- Set up SSL certificate
- Use a proper domain name

---

## ✅ Checklist for Administrators

Before deploying to users:

- [ ] Server is running and accessible
- [ ] Tested with localhost on server computer
- [ ] Tested with IP address on another computer
- [ ] Firewall configured (if needed)
- [ ] Port forwarding configured (if internet access)
- [ ] Documented the correct server URL
- [ ] Created device tokens for all users
- [ ] Prepared clear instructions for users

---

**Remember:** The server URL is the address WHERE YOUR SERVER IS RUNNING, not where the agent is running!

---

**ControlHub Live - Server URL Configuration Guide**

*For more help, see COMPLETE_GUIDE.md*
