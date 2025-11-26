# 📤 GitHub Pe Code Push Karne Ka Tarika

## Step 1: Git Initialize (Agar pehle se nahi kiya)

```bash
git init
```

## Step 2: GitHub Repository Banayein

1. https://github.com pe jayein
2. **"New Repository"** button click karein
3. Repository name enter karein: `deep-night-club`
4. **Public** ya **Private** select karein
5. **"Create Repository"** click karein

## Step 3: Code Add Karein

```bash
# Sab files add karein
git add .

# Commit message likhen
git commit -m "Deep Night Ludo Club - Initial Commit"
```

## Step 4: GitHub Se Connect Karein

```bash
# Apna GitHub repository URL replace karein
git remote add origin https://github.com/YOUR_USERNAME/deep-night-club.git

# Default branch set karein
git branch -M main
```

## Step 5: Push Karein

```bash
# Code push karein
git push -u origin main
```

## ✅ Done!

Ab aapka code GitHub pe hai. Ab aap Koyeb pe deploy kar sakte hain!

---

## 🔧 Agar Error Aaye

### Error: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/deep-night-club.git
```

### Error: "Permission denied"

```bash
# GitHub personal access token use karein
# Settings → Developer Settings → Personal Access Tokens → Generate New Token
```

### Error: "Updates were rejected"

```bash
# Force push (careful - overwrites remote)
git push -u origin main --force
```

---

## 📦 Important Files Jo Push Ho Rahe Hain

- ✅ `backend/Dockerfile` - Backend Docker configuration
- ✅ `frontend/Dockerfile` - Frontend Docker configuration
- ✅ `backend/server.py` - FastAPI backend
- ✅ `frontend/src/` - React frontend
- ✅ `.dockerignore` - Docker ignore file
- ✅ `README.md` - Documentation

---

## 🚀 Next Steps

1. ✓ Code GitHub pe push ho gaya
2. → Koyeb pe deploy karein (KOYEB_DEPLOYMENT.md follow karein)
3. → Environment variables set karein
4. → Test karein
5. → Group mein pin karein

**Good luck! 🎉**
