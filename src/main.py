from pyrogram import Client

import settings
from src.handlers import messages


def build_bot() -> Client:
    bot_app = Client(
        name=settings.BOT_NAME,
        api_id=settings.TELEGRAM_API_ID,
        api_hash=settings.TELEGRAM_API_HASH,
        bot_token=settings.TELEGRAM_BOT_TOKEN
    )
    messages.MessageHandler(bot_app)
    return bot_app


def main():
    bot = build_bot()
    bot.run()


if __name__ == "__main__":
    main()
