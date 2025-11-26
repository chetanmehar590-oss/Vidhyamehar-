# 🚀 Quick Setup Guide - Deep Night Ludo Club

## Step 1: Telegram Bot Token (2 minutes)

1. Telegram mein **@BotFather** search karein
2. `/newbot` bhejein
3. Bot name aur username enter karein
4. **Token save karein** → `1234567890:ABCdefGHI...`

## Step 2: Chat ID (1 minute)

1. Bot ko group mein add karein aur admin banayein
2. Browser mein kholen:
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
3. **Chat ID save karein** → `-1001234567890`

## Step 3: MongoDB (Free) (3 minutes)

1. https://www.mongodb.com/cloud/atlas pe jayein
2. Free account banayein
3. **Connection string save karein**
   ```
   mongodb+srv://user:pass@cluster.mongodb.net/
   ```

## Step 4: Environment Variables

### Backend:
```
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
MONGO_URL=your_mongodb_url
DB_NAME=deep_night_club
```

### Frontend:
```
REACT_APP_BACKEND_URL=your_backend_url
```

## Step 5: Deploy (Koyeb)

1. GitHub pe code push karein
2. Koyeb pe account banayein
3. Repository connect karein
4. Environment variables add karein
5. Deploy!

## Step 6: Test

1. Deployed URL kholen
2. Form bharein (name, amount, etc.)
3. "Send Table" button click karein
4. Telegram group check karein ✅

---

## 📱 Group Setup

1. Web app URL ko group mein message karein
2. Message ko **pin** kar dein
3. Done! Users pinned message click karke table book kar sakte hain

---

## ⚡ Quick Commands

```bash
# Local testing
cd backend && uvicorn server:app --reload
cd frontend && yarn start

# Health check
curl your-backend-url/api/health
```

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| Bot message nahi bhej raha | Bot ko admin banaya? |
| "Failed to send message" | Token/Chat ID check karein |
| CORS error | Backend URL sahi hai? |

---

## ✅ Success Checklist

- [ ] Bot token mila
- [ ] Chat ID mila (negative number)
- [ ] MongoDB setup done
- [ ] Environment variables set
- [ ] Backend deployed
- [ ] Frontend deployed
- [ ] Group mein pinned message
- [ ] Test message successfully sent

---

**Total Time: ~10 minutes** 🎉
