from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from models import TableRequest, TableRequestDB
from telegram_bot import TelegramBot

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection (optional - won't crash if missing)
mongo_url = os.environ.get('MONGO_URL')
if mongo_url:
    client = AsyncIOMotorClient(mongo_url)
    db = client[os.environ.get('DB_NAME', 'deep_night_club')]
else:
    client = None
    db = None
    logging.warning("MongoDB URL not configured - database features disabled")

# Initialize Telegram Bot
telegram_bot = TelegramBot()

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@api_router.get("/")
async def root():
    return {"message": "Deep Night Ludo Club Bot API"}

@api_router.post("/send-table")
async def send_table_request(request: TableRequest):
    """
    Send table request to Telegram group
    """
    try:
        # Save to database
        table_dict = request.dict()
        table_obj = TableRequestDB(**table_dict)
        
        # Send to Telegram
        sent = telegram_bot.send_message(
            username=request.username,
            amount=request.amount,
            type_=request.type,
            game_plus=request.gamePlus,
            options=request.options.dict()
        )
        
        table_obj.sent_to_telegram = sent
        
        # Save to MongoDB (if available)
        if db:
            await db.table_requests.insert_one(table_obj.dict())
        
        if not sent:
            raise HTTPException(
                status_code=500,
                detail="Failed to send message to Telegram. Please check bot configuration."
            )
        
        return {
            "success": True,
            "message": "Table request sent successfully",
            "id": table_obj.id
        }
    
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error processing table request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@api_router.get("/tables")
async def get_all_tables():
    """
    Get all table requests
    """
    if not db:
        return {
            "success": False,
            "tables": [],
            "message": "Database not configured"
        }
    
    try:
        tables = await db.table_requests.find().sort("timestamp", -1).to_list(100)
        # Remove MongoDB _id field to avoid ObjectId serialization issues
        for table in tables:
            if '_id' in table:
                del table['_id']
        return {
            "success": True,
            "tables": tables
        }
    except Exception as e:
        logger.error(f"Error fetching tables: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch tables: {str(e)}"
        )

@api_router.get("/health")
async def health_check():
    """
    Check if bot credentials are configured
    """
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    return {
        "status": "healthy",
        "bot_configured": bool(bot_token and chat_id),
        "database_connected": bool(db is not None),
        "mongo_url_set": bool(mongo_url)
    }

@api_router.post("/send-button-message")
async def send_button_message():
    """
    Send button message to group
    """
    try:
        import requests
        
        bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        chat_id = os.environ.get('TELEGRAM_CHAT_ID')
        
        if not bot_token or not chat_id:
            raise HTTPException(status_code=400, detail="Bot credentials not configured")
        
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        
        payload = {
            "chat_id": chat_id,
            "text": "🎲 DEEP NIGHT LUDO CLUB 🎲\n\nTable book karne ke liye neeche button click karein:",
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "🎲 Place New Table",
                        "web_app": {
                            "url": "https://deep-night-frontend.onrender.com"
                        }
                    }
                ]]
            }
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return {
                "success": True,
                "message": "Button message sent to group!",
                "response": response.json()
            }
        else:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to send message: {response.text}"
            )
    
    except Exception as e:
        logger.error(f"Error sending button message: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# Add root endpoint for health checks
@app.get("/")
async def root_health():
    """Root endpoint for Render health checks"""
    return {
        "status": "online",
        "service": "Deep Night Ludo Club API",
        "api_base": "/api"
    }

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Deep Night Ludo Club Bot API started")
    # Send welcome message if credentials are configured
    if os.environ.get('TELEGRAM_BOT_TOKEN') and os.environ.get('TELEGRAM_CHAT_ID'):
        telegram_bot.send_welcome_message()

@app.on_event("shutdown")
async def shutdown_db_client():
    if client:
        client.close()