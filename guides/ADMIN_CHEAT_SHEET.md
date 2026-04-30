# ControlHub Live - Admin Cheat Sheet

Quick reference for administrators deploying ControlHub Live.

---

## 🚀 Quick Deploy (New Device)

### 1. Create Device
```
Dashboard → Devices → Add Device
Enter name and OS → Create
```

### 2. Download & Share
```
Click "Download Agent" button
Send ZIP + token to user
```

### 3. User Instructions (Copy-Paste)
```
Hi! Here's how to set up monitoring:

1. Extract the ZIP file I sent you
2. Double-click EASY_INSTALL.bat
3. When Notepad opens, paste this token:
   [PASTE TOKEN HERE]
4. Save (Ctrl+S) and close Notepad
5. Double-click START_AGENT.bat
6. Keep the window open

That's it! Let me know when you see "WebSocket connected successfully!"
```

---

## 📊 Dashboard Quick Access

| Page | URL | Purpose |
|------|-----|---------|
| Dashboard | `/dashboard/` | Overview |
| Devices | `/devices/` | Manage devices |
| Users | `/accounts/users/` | Manage users |
| Django Admin | `/admin/` | Full admin |

---

## 🔑 Default Credentials

```
Username: carlomagg
Password: School67@
Role: Super Admin
```

---

## 💻 Common Commands

### Start Server
```bash
start_server.bat
# or
python manage.py runserver 0.0.0.0:8000
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Fix Permissions
```bash
UNLOCK_ADMIN_DASHBOARD.bat
```

### Find Server IP
```bash
ipconfig
# Look for IPv4 Address
```

### Generate Agent ZIP
```bash
python generate_downloadable_agent.py
```

---

## 🌐 Network Setup

### Local Network
```
Server URL: ws://YOUR_LOCAL_IP:8000
Example: ws://192.168.1.100:8000
```

### Internet (Port Forwarding)
```
1. Forward port 8000 on router
2. Find public IP: whatismyipaddress.com
3. Server URL: ws://YOUR_PUBLIC_IP:8000
```

### VPS/Cloud
```
Server URL: wss://your-domain.com
(Requires SSL certificate)
```

---

## 👥 User Roles

| Role | View | Message | Manage Devices | Manage Users |
|------|:----:|:-------:|:--------------:|:------------:|
| Viewer | ✅ | ❌ | ❌ | ❌ |
| Admin | ✅ | ✅ | ✅ | ❌ |
| Super Admin | ✅ | ✅ | ✅ | ✅ |

---

## 🔧 Troubleshooting Quick Fixes

### Device Won't Connect
```
1. Check token is correct
2. Check server is running
3. Check firewall allows port 8000
4. Verify server URL format (ws:// not http://)
```

### Permission Denied
```
Run: UNLOCK_ADMIN_DASHBOARD.bat
Then restart server
```

### Can't Send Messages
```
Check user role is Admin or Super Admin
Run: python check_user_role.py
```

### Port Already in Use
```
netstat -an | findstr :8000
Kill the process or use different port
```

---

## 📱 Mobile Access

```
1. Find server IP: ipconfig
2. On mobile: http://YOUR_IP:8000
3. Login with credentials
4. Tap ☰ menu to navigate
```

---

## 🔐 Security Checklist

- [ ] Change default password
- [ ] Use strong passwords for all users
- [ ] Keep tokens secure
- [ ] Use HTTPS/WSS in production
- [ ] Enable firewall
- [ ] Regular backups
- [ ] Update regularly

---

## 📞 Support Quick Links

| Issue | Check |
|-------|-------|
| Setup problems | COMPLETE_GUIDE.md |
| User instructions | SIMPLE_USER_GUIDE.md |
| Latest features | IMPROVEMENTS_SUMMARY.md |
| Quick commands | QUICK_REFERENCE.md |
| Agent logs | client_agent/agent.log |

---

## 🎯 Deployment Workflow

```
1. Start server (start_server.bat)
2. Create device in dashboard
3. Download agent (click button)
4. Send ZIP + token to user
5. User runs EASY_INSTALL.bat
6. User pastes token
7. User runs START_AGENT.bat
8. Device shows Online ✅
9. Click Monitor to view screen
```

**Time: 3-5 minutes per device**

---

## 📊 Monitoring Best Practices

### Before Deployment
- [ ] Test on your own computer first
- [ ] Document your server URL
- [ ] Create user accounts
- [ ] Test messaging system

### During Deployment
- [ ] Keep tokens organized
- [ ] Label devices clearly
- [ ] Test each connection
- [ ] Document any issues

### After Deployment
- [ ] Monitor device status
- [ ] Check for offline devices
- [ ] Review message logs
- [ ] Gather user feedback

---

## 🚨 Emergency Procedures

### Server Crash
```bash
# Check logs
tail -f agent.log

# Restart server
start_server.bat
```

### Database Issues
```bash
# Backup first!
cp db.sqlite3 db.sqlite3.backup

# Run migrations
python manage.py migrate
```

### Reset Everything
```bash
# DANGER: This deletes all data!
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📈 Scaling Tips

### 10-50 Devices
- Use local network
- Single server
- Standard setup

### 50-200 Devices
- Consider VPS
- Use domain name
- Enable SSL/HTTPS

### 200+ Devices
- Load balancer
- Multiple servers
- Database optimization
- Redis for caching

---

## 🎓 Training Users

### Email Template
```
Subject: Remote Monitoring Setup

Hi [Name],

I'm setting up remote monitoring for your computer.
Here's what you need to do:

1. Download the attached ZIP file
2. Extract it to your Desktop
3. Double-click EASY_INSTALL.bat
4. When Notepad opens, paste this token:
   [TOKEN]
5. Save and close Notepad
6. Double-click START_AGENT.bat

Keep the black window open while working.
You'll see a message saying "WebSocket connected successfully!"

If you have any issues, let me know!

Thanks,
[Your Name]
```

---

## ✅ Daily Checklist

- [ ] Check server is running
- [ ] Review online/offline devices
- [ ] Check for error messages
- [ ] Test monitoring on random device
- [ ] Review message logs
- [ ] Backup database (weekly)

---

## 🔄 Update Procedure

```bash
# Backup first
cp db.sqlite3 db.sqlite3.backup

# Pull updates
git pull

# Update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Restart server
start_server.bat
```

---

## 📞 Quick Support Responses

**"It's not working"**
→ "Can you send me a screenshot of the black window?"

**"Connection refused"**
→ "Is the server running? Check if you can access the dashboard."

**"Invalid token"**
→ "Copy the token again from the device page and paste carefully."

**"Python not found"**
→ "Install Python from python.org and check 'Add to PATH'"

---

## 🎉 Success Metrics

Track these to measure success:

- ⏱️ **Average setup time** (target: <5 minutes)
- ✅ **First-time success rate** (target: >90%)
- 📞 **Support calls per device** (target: <0.2)
- 🟢 **Device uptime** (target: >95%)
- 😊 **User satisfaction** (target: >4/5)

---

**ControlHub Live - Admin Cheat Sheet**

*Keep this handy for quick reference!*

*Last updated: Version 1.1*
