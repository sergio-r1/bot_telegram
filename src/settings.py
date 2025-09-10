from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_NAME = getenv("BOT_NAME")
TELEGRAM_API_ID = getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = getenv("TELEGRAM_API_HASH")
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")