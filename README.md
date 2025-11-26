# Deep Night Ludo Club - Telegram Bot Web App

Yeh ek Telegram bot clone hai jo table booking ke liye design kiya gaya hai.

## Features

- ✅ Beautiful UI matching Telegram Web App design
- ✅ Table booking form with all options
- ✅ Automatic message sending to Telegram group
- ✅ MongoDB database for tracking requests
- ✅ Clean and responsive design

## Setup Instructions for Koyeb

### Environment Variables Required

Koyeb pe deployment karte waqt yeh environment variables set karna zaroori hai:

```
# Backend Variables
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
MONGO_URL=your_mongodb_url
DB_NAME=deep_night_club

# Frontend Variables
REACT_APP_BACKEND_URL=your_backend_url_here
```

### How to Get Telegram Credentials

#### 1. Bot Token Kaise Banaye:
1. Telegram pe @BotFather ko search karein
2. `/newbot` command bhejein
3. Bot ka naam enter karein (e.g., "Deep Night Club Bot")
4. Bot ka username enter karein (e.g., "DeepNightClubBot")
5. BotFather aapko token dega (format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### 2. Chat ID Kaise Nikale:
1. Apne bot ko group mein add karein
2. Bot ko admin banayein
3. Is URL pe jaaein (apna bot token dalein):
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. Response mein "chat":{"id": -1001234567890} milega
5. Yeh number aapka CHAT_ID hai

### Group Mein Button Pin Karna

1. Apne web app ka URL pin karein group mein
2. Message format:
   ```
   🎲 Place New Table
   [Your Web App URL]
   ```
3. Message ko pin kar dein

### Message Format

Jab user form submit karega, group mein aise message aayega:

```
Table by Username:
2000 | Full | 7+ game

==>No iPhone
```

## Local Development

```bash
# Backend
cd backend
python server.py

# Frontend
cd frontend
yarn start
```

## Tech Stack

- **Frontend**: React + Tailwind CSS + shadcn/ui
- **Backend**: FastAPI + Python
- **Database**: MongoDB
- **Integration**: Telegram Bot API

## Support

Agar koi problem ho to bot configuration check karein aur logs dekhein.
