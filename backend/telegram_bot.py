import os
import requests
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.environ.get('TELEGRAM_CHAT_ID')
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    def format_table_message(self, username: str, amount: str, type_: str, game_plus: str, options: Dict[str, bool]) -> str:
        """Format table message like in the screenshot"""
        # Format options
        selected_options = []
        if options.get('freshId'):
            selected_options.append('Fresh Id')
        if options.get('codeAapDoge'):
            selected_options.append('Code Aap Doge')
        if options.get('noIPhone'):
            selected_options.append('No iPhone')
        if options.get('noKingPass'):
            selected_options.append('No King Pass')
        if options.get('autoLoss'):
            selected_options.append('Auto Loss')

        # Build message
        message = f"Table by {username}:\n"
        message += f"{amount} | {type_} | {game_plus} game\n"
        
        if selected_options:
            message += "\n==>"
            message += "==>".join(selected_options)
        
        return message

    def send_message(self, username: str, amount: str, type_: str, game_plus: str, options: Dict[str, bool]) -> bool:
        """Send table request to Telegram group"""
        try:
            if not self.bot_token or not self.chat_id:
                logger.error("Telegram credentials not configured")
                return False

            message = self.format_table_message(username, amount, type_, game_plus, options)
            
            url = f"{self.base_url}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }

            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                logger.info(f"Message sent successfully by {username}")
                return True
            else:
                logger.error(f"Failed to send message: {response.text}")
                return False

        except Exception as e:
            logger.error(f"Error sending Telegram message: {str(e)}")
            return False

    def send_welcome_message(self) -> bool:
        """Send welcome message to verify bot connection"""
        try:
            if not self.bot_token or not self.chat_id:
                return False

            url = f"{self.base_url}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': '🎲 Deep Night Ludo Club Bot is now active! 🎲\n\nReady to receive table requests.',
                'parse_mode': 'HTML'
            }

            response = requests.post(url, json=payload, timeout=10)
            return response.status_code == 200

        except Exception as e:
            logger.error(f"Error sending welcome message: {str(e)}")
            return False