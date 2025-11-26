# 🤖 Telegram Bot Setup - Group Only Web App

## Step 1: BotFather Se Bot Setup

### 1. Bot Banayein (Agar already nahi hai)
```
/newbot
Name: Deep Night Ludo Club Bot
Username: DeepNightClubBot
```

### 2. Web App URL Set Karein
```
/newapp
Select your bot: @DeepNightClubBot
Title: Place New Table
Description: Book your ludo table
Web App URL: [Your deployed frontend URL]
Photo: [Optional - upload dice/ludo image]
```

Isse ek button "Place New Table" ban jayega

### 3. Bot Commands Disable Karein (Khali Bot)
```
/setcommands
Select your bot
Send: (empty - press send without typing)
```

## Step 2: Group Mein Bot Setup

### 1. Bot Ko Group Mein Add Karein
- Apne group mein jayein
- Add members → Bot search karein
- Add karein

### 2. Bot Ko Admin Banayein
- Group info → Administrators
- Add Administrator
- Bot select karein
- Permissions:
  ✅ Post Messages
  ✅ Delete Messages (optional)

### 3. Web App Button Group Mein Pin Karein

Option A - Manual Message:
```
Group mein type karein:
🎲 Place New Table 🎲
```
Phir bot mention karein aur "Place New Table" button automatically dikhe ga

Option B - Bot Command (if enabled):
```
/start Place New Table
```

## Step 3: Web App Ko Group-Only Banayein

Frontend code mein yeh check hoga:
- Telegram.WebApp.initDataUnsafe.chat.type === 'group'
- Agar group se nahi khula to error dikhe ga

## Testing

1. Group se button click karein → Form khule ga ✅
2. Bot directly open karein → Khali ✅
3. Form submit karein → Group mein message ✅

---

**Note:** Main ab frontend code update kar raha hoon taaki:
1. Sirf group se hi form open ho
2. Bot bahar se khali dikhe
3. Messages automatically group mein jaye
