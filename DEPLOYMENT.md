# 🚀 Railway Deployment Guide

## Quick Deploy Steps

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Ready for Railway deployment"
git branch -M main
git remote add origin https://github.com/carlomagg/controlhub.git
git push -u origin main
```

### 2. Deploy on Railway

1. Go to [railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose **carlomagg/controlhub**
6. Railway will auto-detect and deploy!

### 3. Access Your App

After deployment (2-3 minutes):
- Railway will give you a URL like: `https://controlhub-production.up.railway.app`
- Click the URL to access your dashboard

### 4. Default Login Credentials

**Username:** `admin`  
**Password:** `admin123`

⚠️ **IMPORTANT:** Change this password immediately after first login!

---

## 🔧 Optional: Custom Admin Credentials

If you want custom credentials, add these environment variables in Railway:

1. Go to your project in Railway
2. Click **"Variables"** tab
3. Add these:
   - `DJANGO_SUPERUSER_USERNAME` = your_username
   - `DJANGO_SUPERUSER_EMAIL` = your_email
   - `DJANGO_SUPERUSER_PASSWORD` = your_password

4. Redeploy the app

---

## 📱 Connecting Client Agents

After deployment, update your client agents:

1. Download agent from: `https://your-app.railway.app/devices/download-agent/`
2. Edit `agent_config.json`:
```json
{
    "server_url": "https://your-app.railway.app",
    "device_id": "your-device-id",
    "api_key": "your-api-key"
}
```

---

## 🎯 Demo Tips

For client demos:
- Use the Railway URL (looks professional)
- Create demo user accounts with viewer role
- Show real-time screen monitoring
- Demonstrate messaging features
- Show multi-device management

---

## 💰 Railway Free Tier

- $5 free credit per month
- Enough for testing and demos
- Upgrade anytime for production use

---

## 🆘 Troubleshooting

**App won't start?**
- Check Railway logs in the dashboard
- Verify all files were pushed to GitHub

**Can't login?**
- Use default credentials: admin/admin123
- Check Railway logs for superuser creation message

**WebSockets not working?**
- Railway supports WebSockets by default
- Check browser console for errors

---

## 📞 Support

Need help? Check the logs in Railway dashboard or review the main README.md
