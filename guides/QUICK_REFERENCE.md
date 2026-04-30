# ControlHub Live - Quick Reference

## 🚀 Quick Commands

### Setup (First Time)
```bash
# Windows
setup.bat

# Linux/macOS
chmod +x setup.sh && ./setup.sh
```

### Start Server
```bash
# Windows
start_server.bat

# Linux/macOS
./start_server.sh

# Manual
python manage.py runserver 0.0.0.0:8000
# or
daphne -b 0.0.0.0 -p 8000 controlhub.asgi:application
```

### Start Client Agent
```bash
cd client_agent
python agent.py
```

---

## 🔑 Default Access

- **Dashboard:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin
- **Default User:** admin (created during setup)

---

## 📝 Common Tasks

### Create Superuser
```bash
python manage.py createsuperuser
python manage.py shell
>>> from accounts.models import User
>>> user = User.objects.get(username='admin')
>>> user.role = 'super_admin'
>>> user.save()
>>> exit()
```

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Create Device
1. Login to dashboard
2. Devices → Add Device
3. Copy token
4. Configure `client_agent/agent_config.json`

---

## ⚙️ Configuration Files

### Server: `controlhub/settings.py`
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
SECRET_KEY = 'your-secret-key'
```

### Agent: `client_agent/agent_config.json`
```json
{
    "server_url": "ws://YOUR_SERVER_IP:8000",
    "device_token": "your-token",
    "capture_interval": 0.5,
    "jpeg_quality": 60
}
```

---

## 🔧 Troubleshooting

### Server won't start
```bash
# Check port
netstat -an | grep 8000

# Check logs
python manage.py runserver
```

### Agent won't connect
```bash
# Check config
cat client_agent/agent_config.json

# Check logs
tail -f client_agent/agent.log

# Test connection
ping your-server-ip
```

### Device shows offline
- Restart agent
- Check device token
- Verify server is running
- Check firewall

---

## 📊 User Roles

| Role | View | Message | Manage Devices | Manage Users |
|------|:----:|:-------:|:--------------:|:------------:|
| Viewer | ✅ | ❌ | ❌ | ❌ |
| Admin | ✅ | ✅ | ✅ | ❌ |
| Super Admin | ✅ | ✅ | ✅ | ✅ |

---

## 🌐 URLs

- Dashboard: `/dashboard/`
- Devices: `/devices/`
- Users: `/accounts/users/`
- Admin: `/admin/`
- Device WS: `/ws/device/{token}/`
- Monitor WS: `/ws/monitor/{id}/`

---

## 📦 Dependencies

### Server
- Django 6.0.4
- channels 4.3.2
- daphne 4.2.1
- djangorestframework 3.17.1

### Agent
- websocket-client 1.9.0
- mss 10.2.0
- pillow 12.2.0
- psutil 6.1.1

---

## 🔒 Security Checklist

- [ ] Change SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use HTTPS/WSS in production
- [ ] Enable firewall
- [ ] Use strong passwords
- [ ] Keep tokens secure
- [ ] Regular updates

---

## 📈 Performance Tips

**Low Bandwidth:**
```json
{
    "capture_interval": 1.0,
    "jpeg_quality": 40,
    "screen_width": 800
}
```

**High Quality:**
```json
{
    "capture_interval": 0.2,
    "jpeg_quality": 80,
    "screen_width": 1920
}
```

---

## 🆘 Emergency Commands

### Stop All
```bash
# Kill server
pkill -f daphne
pkill -f "python manage.py runserver"

# Kill agent
pkill -f "python agent.py"
```

### Reset Database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### View Logs
```bash
# Agent logs
tail -f client_agent/agent.log

# Server logs (if using supervisor)
sudo supervisorctl tail -f controlhub
```

---

**For complete documentation, see [SETUP_GUIDE.md](SETUP_GUIDE.md)**
