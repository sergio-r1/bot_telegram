from pyrogram import Client

import settings


def main():
    app = Client(
        name=settings.BOT_NAME,
        api_id=settings.TELEGRAM_API_ID,
        api_hash=settings.TELEGRAM_API_HASH,
        bot_token=settings.TELEGRAM_BOT_TOKEN
    )
    app.run()


if __name__ == "__main__":
    main()
