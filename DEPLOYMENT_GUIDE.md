# Deep Night Ludo Club - Complete Deployment Guide

## 📱 Kya Banaya Gaya Hai?

Yeh ek **Telegram Web App** hai jo Ludo table booking ke liye design kiya gaya hai. Jab user form bharega aur "Send Table" button press karega, to automatically message aapke Telegram group mein send ho jayega.

## 🎯 Features

✅ Beautiful UI matching Telegram Web App design  
✅ Table booking form with:
   - Amount selection (quick buttons + custom input)
   - Type selection (Full/Half/Quick)
   - Game+ options
   - Options (Fresh Id, Code aap doge, No iPhone, No king pass, Auto loss)
✅ Automatic message sending to Telegram group  
✅ MongoDB database for tracking all requests  
✅ User-friendly interface with icons  

## 📋 Prerequisites

Before deployment, aapko yeh cheezein chahiye:

1. **Telegram Bot Token** (BotFather se)
2. **Telegram Group Chat ID**
3. **MongoDB Database** (Atlas ya local)
4. **Hosting Platform** (Koyeb, Heroku, Railway, etc.)

---

## 🤖 Step 1: Telegram Bot Setup

### 1.1 Bot Create Karna

1. Telegram app open karein
2. **@BotFather** search karein aur message bhejein
3. `/newbot` command bhejein
4. Bot ka naam enter karein:
   ```
   Deep Night Club Bot
   ```
5. Bot ka username enter karein (unique hona chahiye):
   ```
   DeepNightClubBot
   ```
6. BotFather aapko **Bot Token** dega, isko save kar lein:
   ```
   Format: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567
   ```

### 1.2 Group Create/Setup Karna

1. Telegram pe ek **new group** banayein ya existing group use karein
2. Apne bot ko group mein **add** karein:
   - Group info → Add members → Bot search karein
3. Bot ko **Admin** banayein:
   - Group info → Edit → Administrators → Add Administrator
   - Bot ko select karein aur admin banayein

### 1.3 Chat ID Nikalna

**Method 1: getUpdates API**

1. Group mein koi bhi message bhejein (kuch bhi likh sakte hain)
2. Browser mein yeh URL kholen (apna bot token dalein):
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
3. Response mein yeh format milega:
   ```json
   {
     "ok": true,
     "result": [
       {
         "message": {
           "chat": {
             "id": -1001234567890,
             "title": "Deep Night Club"
           }
         }
       }
     ]
   }
   ```
4. `chat.id` ko copy kar lein (negative number hoga)

**Method 2: @RawDataBot**

1. @RawDataBot ko group mein add karein
2. Bot automatically chat ID send karega
3. Bot ko remove kar dein

---

## 💾 Step 2: MongoDB Setup

### Option 1: MongoDB Atlas (Recommended for Cloud)

1. https://www.mongodb.com/cloud/atlas pe jayein
2. Free account banayein
3. "Create a New Cluster" → Free tier select karein
4. Cluster ready hone ke baad:
   - "Connect" button click karein
   - "Connect your application" select karein
   - Connection string copy karein:
     ```
     mongodb+srv://username:password@cluster.mongodb.net/
     ```

### Option 2: Local MongoDB

```bash
# Install MongoDB locally
# Ubuntu/Debian
sudo apt-get install mongodb

# macOS
brew install mongodb-community

# Start MongoDB
sudo systemctl start mongodb  # Linux
brew services start mongodb-community  # macOS
```

---

## 🚀 Step 3: Koyeb Deployment

### 3.1 Code Push to GitHub

```bash
# Git repository banayein
git init
git add .
git commit -m "Deep Night Club Bot"
git branch -M main
git remote add origin https://github.com/yourusername/deep-night-club.git
git push -u origin main
```

### 3.2 Koyeb Setup

1. https://www.koyeb.com pe jayein aur sign up karein
2. Dashboard → "Create App" click karein
3. **GitHub** select karein aur repository connect karein

### 3.3 Backend Service Setup

1. **Service Name**: `deep-night-backend`
2. **Builder**: Docker
3. **Dockerfile Path**: `backend/Dockerfile` (agar nahi hai to neeche dekhen)
4. **Port**: `8001`
5. **Environment Variables** add karein:
   ```
   TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   TELEGRAM_CHAT_ID=-1001234567890
   MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
   DB_NAME=deep_night_club
   ```

### 3.4 Frontend Service Setup

1. **Service Name**: `deep-night-frontend`
2. **Builder**: Docker
3. **Dockerfile Path**: `frontend/Dockerfile`
4. **Port**: `3000`
5. **Environment Variables**:
   ```
   REACT_APP_BACKEND_URL=https://deep-night-backend.koyeb.app
   ```

### 3.5 Dockerfiles (Agar nahi hain to create karein)

**Backend Dockerfile** (`/app/backend/Dockerfile`):
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
```

**Frontend Dockerfile** (`/app/frontend/Dockerfile`):
```dockerfile
FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
```

**Frontend nginx.conf**:
```nginx
server {
    listen 3000;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

---

## 📱 Step 4: Telegram Group Mein Setup

### 4.1 Pinned Message Create Karna

1. Group mein ek message bhejein:
   ```
   🎲 Place New Table
   
   Click the button below to book your table:
   https://deep-night-frontend.koyeb.app
   ```

2. Message ko **pin** kar dein:
   - Message pe long press → Pin

### 4.2 User Flow

1. User pinned message pe click karega
2. Web app browser mein khulega
3. User details bharega:
   - Name
   - Amount
   - Type (Full/Half/Quick)
   - Game+
   - Options select karega
4. "Send Table" button press karega
5. **Automatic message group mein send ho jayega**:
   ```
   Table by Rahul:
   2000 | Full | 7+ game
   
   ==>No iPhone
   ```

---

## 🧪 Testing

### Local Testing

1. `.env` file create karein aur credentials fill karein
2. Backend start karein:
   ```bash
   cd backend
   uvicorn server:app --reload
   ```
3. Frontend start karein:
   ```bash
   cd frontend
   yarn start
   ```
4. Browser mein `http://localhost:3000` kholen
5. Form bharein aur test karein

### Production Testing

1. Deployed URL kholen
2. Sample data fill karein
3. "Send Table" button press karein
4. Telegram group check karein - message aana chahiye

---

## 📊 Message Format

Group mein jo message ayega, wo kuch aise dikhega:

```
Table by Username:
amount | type | game+ game

==>Option1==>Option2==>Option3
```

**Example**:
```
Table by Rahul:
2000 | Full | 7+ game

==>No iPhone
```

---

## 🔧 Troubleshooting

### Issue 1: Bot message nahi bhej raha

**Solutions**:
- Bot ko group mein admin banaya hai?
- Bot token sahi hai?
- Chat ID negative number hai aur sahi hai?
- Backend logs check karein

### Issue 2: "Failed to send message to Telegram"

**Check**:
```bash
# Backend logs dekhen
curl https://your-backend-url.koyeb.app/api/health
```

Response:
```json
{
  "status": "healthy",
  "bot_configured": true,
  "database_connected": true
}
```

### Issue 3: CORS Error

Frontend ke `.env` mein `REACT_APP_BACKEND_URL` correct hai?

---

## 📝 Environment Variables Summary

### Backend `.env`:
```env
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
MONGO_URL=your_mongodb_url
DB_NAME=deep_night_club
```

### Frontend `.env`:
```env
REACT_APP_BACKEND_URL=https://your-backend-url.com
```

---

## 🎉 Success!

Agar sab kuch sahi se setup ho gaya hai to:

✅ Users pinned link click karenge  
✅ Form bharenge  
✅ Message automatically group mein send hoga  
✅ Database mein save hoga  

---

## 🆘 Support

Agar koi problem ho to:

1. Backend health endpoint check karein: `/api/health`
2. Telegram bot token verify karein
3. Chat ID double-check karein
4. Logs dekhein (backend aur frontend dono)

---

## 🔐 Security Tips

1. Environment variables ko **kabhi** public nahi karein
2. `.env` file ko `.gitignore` mein add karein
3. Bot token ko secure rakhein
4. MongoDB Atlas mein IP whitelist use karein

---

## 📞 Additional Features (Future)

- [ ] Table request history
- [ ] User profile management
- [ ] Payment integration
- [ ] Auto-matching system
- [ ] Real-time notifications

---

**Made with ❤️ for Deep Night Ludo Club**
