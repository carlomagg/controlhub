# ControlHub Live - Simple User Guide
## For People Being Monitored

---

## 📋 What You Need

Your administrator will give you:
1. **A ZIP file** (client_agent.zip)
2. **A token** (long code like: xYz123AbC456...)
3. **Server URL** (like: ws://192.168.1.100:8000 or wss://controlhub.yourcompany.com)

---

## 🚀 Setup in 3 Easy Steps

### Step 1: Extract the ZIP File
- Right-click the ZIP file
- Click "Extract All"
- Choose Desktop or any folder
- Click "Extract"

### Step 2: Install & Configure
1. Open the extracted folder
2. **Double-click** `EASY_INSTALL.bat`
3. Wait for installation (takes 1-2 minutes)
4. **Notepad will open automatically**
5. Find the line that says: `"device_token": "PASTE_TOKEN_HERE"`
6. Replace `PASTE_TOKEN_HERE` with your actual token
7. Find the line that says: `"server_url": "PASTE_SERVER_URL_HERE"`
8. Replace `PASTE_SERVER_URL_HERE` with your server URL (the URL where your company hosts the app - NOT localhost)
9. Press **Ctrl+S** to save
10. Close Notepad

**Important:** The server URL should be the actual address where your company's ControlHub is hosted (e.g., ws://192.168.1.100:8000 or wss://controlhub.yourcompany.com), NOT ws://localhost:8000

### Step 3: Start Monitoring
1. **Double-click** `START_AGENT.bat`
2. A black window will open
3. You should see: **"WebSocket connected successfully!"**
4. **Keep this window open!**

✅ **Done!** You're now being monitored.

---

## 🛑 To Stop Monitoring

Simply **close the black window** (Command Prompt)

---

## ❓ Frequently Asked Questions

**Q: What is being monitored?**  
A: Your screen - everything you see on your monitor.

**Q: Will it slow down my computer?**  
A: No, it uses very little resources.

**Q: Can I still use my computer normally?**  
A: Yes! You won't notice any difference.

**Q: Who can see my screen?**  
A: Only administrators with access to the dashboard.

**Q: Can I stop it anytime?**  
A: Yes! Just close the black window.

**Q: Will it run when I restart my computer?**  
A: No, you need to start it again manually.

**Q: What if I see a popup message?**  
A: That's your administrator sending you a message. Read it and click OK.

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"
**Solution:**
1. Install Python from: https://www.python.org/downloads/
2. During installation, check ☑ "Add Python to PATH"
3. Restart your computer
4. Try again

### Problem: "Connection refused"
**Solution:**
- Check with your administrator
- Make sure the server URL is correct
- Check your internet connection

### Problem: "Invalid token"
**Solution:**
- Copy the token again from your administrator
- Make sure there are no extra spaces
- Paste it carefully in the config file

### Problem: Black window closes immediately
**Solution:**
- Open `agent_config.json` with Notepad
- Check that token and server URL are correct
- Make sure you saved the file (Ctrl+S)

---

## 📞 Need Help?

Contact your system administrator or IT support.

**Include this information when asking for help:**
- What step you're on
- What error message you see (if any)
- Screenshot of the black window (if it shows an error)

---

## 🔐 Privacy & Security

- ✅ Only authorized administrators can view your screen
- ✅ The agent must be running for monitoring to work
- ✅ You can stop monitoring anytime
- ✅ Your device token is unique and secure
- ✅ No data is stored on your computer
- ✅ Everything is transmitted securely

---

## 📝 Quick Reference

**To Start Monitoring:**
```
Double-click: START_AGENT.bat
Keep window open
```

**To Stop Monitoring:**
```
Close the black window
```

**Configuration File:**
```
agent_config.json
(Open with Notepad to edit)
```

**Log File:**
```
agent.log
(Check this if you have problems)
```

---

## ✅ Success Checklist

- [ ] Extracted ZIP file
- [ ] Ran EASY_INSTALL.bat
- [ ] Pasted token in config file
- [ ] Pasted server URL in config file
- [ ] Saved config file (Ctrl+S)
- [ ] Ran START_AGENT.bat
- [ ] Saw "WebSocket connected successfully!"
- [ ] Kept black window open

**If all checked, you're done!** ✨

---

**ControlHub Live - Professional Remote Monitoring Made Simple**

*This guide is for end users. For administrator documentation, see COMPLETE_GUIDE.md*
