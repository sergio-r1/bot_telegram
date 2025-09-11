from enum import Enum

from pyrogram import Client, filters

__all__ = ["MessageHandler"]


class MessageType(Enum):
    COMMAND = "command"
    MEDIA = "media"
    TEXT = "text"


class MessageHandler:
    DEFAULT_RESPONSE = "Support to {0} not implemented yet"
    
    def __init__(self, client: Client):
        self.app = client
        self.setup_handlers()

    def setup_handlers(self) -> None:
        # Command handlers
        self.app.on_message(filters.command('start'))(self.handle_start)
        self.app.on_message(filters.command('help'))(self.handle_help)

        # Media handlers
        self.app.on_message(filters.audio | filters.voice)(self.handle_audio)
        self.app.on_message(filters.photo)(self.handle_photo)
        self.app.on_message(filters.sticker)(self.handle_sticker)
        self.app.on_message(filters.video | filters.animation)(self.handle_video)

        # Text handlers
        self.app.on_message()(self.handle_text)
        self.app.on_message(filters.document)(self.handle_document)
    
    async def handle_start(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("start"))

    async def handle_help(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("help"))

    async def handle_audio(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("audio"))

    async def handle_document(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("documents"))

    async def handle_photo(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("photo"))

    async def handle_sticker(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("sticker"))

    async def handle_video(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("video"))

    async def handle_text(self, client: Client, message):
        await message.reply(self.DEFAULT_RESPONSE.format("text"))

