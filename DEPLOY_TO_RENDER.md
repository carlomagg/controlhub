# 🚀 Deploy to Render - Step by Step

## ✅ Your App is Ready for Render!

All configuration files are set up:
- ✅ `render.yaml` - Render configuration
- ✅ `build.sh` - Build script
- ✅ Auto superuser creation enabled
- ✅ All dependencies configured

---

## 📋 Deploy Now (5 Minutes)

### Step 1: Go to Render
Visit: **https://render.com**

### Step 2: Sign Up/Login
- Click **"Get Started"** or **"Sign In"**
- Sign in with your **GitHub** account

### Step 3: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**

### Step 4: Connect Repository
1. Click **"Connect account"** if needed
2. Find and select: **carlomagg/controlhub**
3. Click **"Connect"**

### Step 5: Configure Service
Render will auto-detect settings from `render.yaml`, but verify:

- **Name:** `controlhub` (or your choice)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Build Command:** 
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- **Start Command:**
  ```
  python manage.py create_superuser_if_none && daphne -b 0.0.0.0 -p $PORT controlhub.asgi:application
  ```
- **Plan:** **Free**

### Step 6: Deploy!
1. Click **"Create Web Service"**
2. Wait 3-5 minutes for build and deployment
3. Watch the logs for progress

---

## 🔐 Login Credentials

Once deployed, access your app at the Render URL:

**Username:** `admin`  
**Password:** `admin123`

⚠️ **IMPORTANT:** Change this password after first login!

---

## 📱 After Deployment

### 1. Test Your App
- Visit your Render URL (e.g., `https://controlhub.onrender.com`)
- Login with admin/admin123
- Create a test device
- Verify dashboard works

### 2. Update Client Agents
Edit `agent_config.json` on client machines:
```json
{
    "server_url": "https://your-app.onrender.com",
    "device_id": "your-device-id",
    "api_key": "your-api-key"
}
```

### 3. For Client Demos
- Create demo user accounts (viewer role)
- Add demo devices
- Show real-time monitoring
- Demonstrate messaging features

---

## 🔧 Troubleshooting

### Build Failed?
- Check Render logs (click "Logs" tab)
- Look for error messages
- Common issues already fixed:
  - ✅ Dependencies installed
  - ✅ Python version set
  - ✅ Static files configured

### App Not Loading?
- Wait 30 seconds after "Live" status
- Check if deployment is "Active"
- Verify URL is correct (HTTPS)

### Can't Login?
- Use: `admin` / `admin123`
- Check logs for "Superuser created successfully!"
- Try creating user manually via Render shell

### WebSockets Not Working?
- Render supports WebSockets on all plans
- Check browser console (F12) for errors
- Verify using HTTPS (not HTTP)

---

## 💰 Render Free Tier

**Free Plan Includes:**
- ✅ 750 hours/month (enough for 24/7)
- ✅ Automatic HTTPS
- ✅ WebSocket support
- ✅ Auto-deploy from GitHub
- ⚠️ Spins down after 15 min of inactivity
- ⚠️ Takes ~30 sec to wake up

**Upgrade Options:**
- $7/month - No spin down, faster
- Perfect for production use

---

## 🎯 Important Notes

1. **Free tier sleeps** - First request after inactivity takes 30 seconds
2. **Database** - Using SQLite (resets on redeploy). For production, upgrade to PostgreSQL
3. **Static files** - Handled by WhiteNoise
4. **WebSockets** - Fully supported on all plans

---

## 🎉 You're All Set!

Your app is ready to deploy on Render. Just follow the steps above!

**Repository:** https://github.com/carlomagg/controlhub.git  
**Render:** https://render.com

---

## 📞 Need Help?

If deployment fails, check:
1. Render deployment logs
2. Verify GitHub repo is up to date
3. Check this guide again
