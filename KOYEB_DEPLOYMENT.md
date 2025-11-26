# 🚀 Koyeb Deployment Guide - Docker Method

## ✅ Prerequisites

1. ✓ Dockerfiles banaye gaye hain (`backend/Dockerfile` aur `frontend/Dockerfile`)
2. ✓ Code GitHub pe push kar diya hai
3. ✓ Telegram Bot Token ready hai
4. ✓ Telegram Chat ID ready hai
5. ✓ MongoDB URL ready hai

---

## 📦 STEP 1: Backend Service Deploy

### 1. Koyeb Dashboard pe jayein
- https://app.koyeb.com/

### 2. "Create App" ya "Create Service" click karein

### 3. GitHub Repository Select karein
- Repository: `your-username/deep-night-club` (ya jo bhi naam hai)

### 4. Service Settings:

**Builder:**
```
Docker
```

**Dockerfile Path:**
```
backend/Dockerfile
```

**Service Name:**
```
deep-night-backend
```

**Port:**
```
8000
```

### 5. Environment Variables Add karein:

Click **"Add Environment Variable"** aur ek ek kar ke yeh 4 variables add karein:

```
Variable 1:
Name: TELEGRAM_BOT_TOKEN
Value: 7898765432:AAHxyzABC123defGHI456jklMNO789pqrSTU
(Apna actual token yahaan paste karein)

Variable 2:
Name: TELEGRAM_CHAT_ID
Value: -1001234567890
(Apna actual chat ID yahaan - negative number hona chahiye)

Variable 3:
Name: MONGO_URL
Value: mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
(Apna MongoDB Atlas URL yahaan)

Variable 4:
Name: DB_NAME
Value: deep_night_club
```

### 6. Deploy Click karein

Wait karein 2-3 minutes. Backend deploy hone ke baad aapko URL milega:
```
https://deep-night-backend-xyz123.koyeb.app
```

**✅ IS URL KO COPY KAR LEIN - Frontend mein use hoga!**

---

## 🎨 STEP 2: Frontend Service Deploy

### 1. Phir se "Create App" ya "Create Service" click karein

### 2. Same GitHub Repository Select karein

### 3. Service Settings:

**Builder:**
```
Docker
```

**Dockerfile Path:**
```
frontend/Dockerfile
```

**Service Name:**
```
deep-night-frontend
```

**Port:**
```
3000
```

### 4. Environment Variable Add karein:

**IMPORTANT:** Backend ka URL use karein (jo upar copy kiya tha)

```
Name: REACT_APP_BACKEND_URL
Value: https://deep-night-backend-xyz123.koyeb.app
```

**Note:** 
- Trailing slash `/` NAHI lagana
- `/api` NAHI lagana
- Sirf base URL paste karein

### 5. Deploy Click karein

Wait karein 3-4 minutes. Frontend deploy hone ke baad URL milega:
```
https://deep-night-frontend-abc789.koyeb.app
```

---

## 📱 STEP 3: Telegram Group Setup

### 1. Group mein Message bhejein:

```
🎲 DEEP NIGHT LUDO CLUB 🎲

Table book karne ke liye neeche link click karein:
https://deep-night-frontend-abc789.koyeb.app

📋 Instructions:
• Amount select karein
• Type choose karein (Full/Half/Quick)
• Game+ value enter karein
• Options select karein (optional)
• Send Table button press karein

✅ Message automatically is group mein send ho jayega!
```

### 2. Is message ko **PIN** kar dein:
- Message pe long press → Pin option select karein

---

## 🧪 STEP 4: Testing

### Test 1: Backend Health Check

Browser mein yeh URL kholen:
```
https://deep-night-backend-xyz123.koyeb.app/api/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "bot_configured": true,
  "database_connected": true
}
```

Agar `bot_configured: false` dikhta hai to:
- Environment variables check karein
- Deployment phir se karein

### Test 2: Frontend Check

Browser mein frontend URL kholen:
```
https://deep-night-frontend-abc789.koyeb.app
```

Form dikhna chahiye with:
- Amount input
- Type dropdown
- Game+ input
- Options checkboxes
- Send Table button

### Test 3: Full Flow Test

1. Frontend URL kholen
2. Form bharein:
   - Amount: `2000`
   - Type: `Full`
   - Game+: `7+`
   - Option: `No iPhone` check karein
3. **Send Table** button press karein
4. Telegram group check karein

**Expected Message in Group:**
```
Table by User:
2000 | Full | 7+ game

==>No iPhone
```

---

## 🔍 Troubleshooting

### Issue 1: Backend Deploy Fail

**Logs Check karein:**
- Koyeb dashboard → Service → Logs tab

**Common Fixes:**
- Environment variables sahi hain?
- Dockerfile path correct hai? (`backend/Dockerfile`)
- Port 8000 set hai?

### Issue 2: Frontend Deploy Fail

**Check:**
- Dockerfile path: `frontend/Dockerfile`
- Port 3000 set hai?
- `REACT_APP_BACKEND_URL` correct hai?

### Issue 3: "Failed to send message to Telegram"

**Verify:**
1. Bot token sahi hai?
2. Chat ID negative number hai?
3. Bot group mein hai aur admin hai?
4. Backend health check pass ho raha hai?

### Issue 4: CORS Error

**Solution:**
- Frontend env variable check karein
- Backend URL mein `/api` ya trailing `/` nahi hona chahiye
- Browser cache clear karein

---

## 📊 Deployment Checklist

- [ ] Backend Dockerfile created
- [ ] Frontend Dockerfile created
- [ ] Code pushed to GitHub
- [ ] Backend service deployed on Koyeb
- [ ] Backend environment variables set (4 variables)
- [ ] Backend health check passing
- [ ] Frontend service deployed on Koyeb
- [ ] Frontend environment variable set (1 variable)
- [ ] Frontend loading correctly
- [ ] Message pinned in Telegram group
- [ ] Bot is admin in group
- [ ] Full flow test successful

---

## 🎉 Success Indicators

✅ Backend URL responding  
✅ Frontend loading properly  
✅ Form submission working  
✅ Messages appearing in Telegram group  
✅ Data saving in MongoDB  

---

## 📝 Important URLs

**Backend:**
```
https://your-backend.koyeb.app/api/health
https://your-backend.koyeb.app/api/tables
```

**Frontend:**
```
https://your-frontend.koyeb.app
```

**Telegram Group:**
```
Your group link here
```

---

## 🆘 Need Help?

1. Backend logs check karein
2. Frontend browser console check karein
3. Network tab dekhen (browser DevTools)
4. Environment variables re-verify karein

---

**Made with ❤️ for Deep Night Ludo Club**
