import requests
import os

# Apne credentials yahaan dalein
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # BotFather se mila token
CHAT_ID = "YOUR_CHAT_ID_HERE"      # Group ka chat ID (negative number)
WEB_APP_URL = "https://deep-night-frontend.onrender.com"

def send_button_message():
    """Send message with button to group"""
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    # Message with inline button
    payload = {
        "chat_id": CHAT_ID,
        "text": "🎲 DEEP NIGHT LUDO CLUB 🎲\n\nTable book karne ke liye neeche button click karein:",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🎲 Place New Table",
                        "web_app": {"url": WEB_APP_URL}
                    }
                ]
            ]
        }
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("✅ Message with button sent successfully!")
        print(f"Response: {response.json()}")
    else:
        print(f"❌ Error: {response.text}")

if __name__ == "__main__":
    send_button_message()
