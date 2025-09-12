from unittest.mock import AsyncMock, MagicMock

import pytest

from src.handlers.messages import MessageHandler


@pytest.fixture
def mock_client():
    # Mock dos métodos on_message do Pyrogram.
    mock = MagicMock()
    mock.on_message.side_effect = lambda filt=None: lambda func: func
    return mock


@pytest.fixture
def message_mock():
    message = MagicMock()
    message.reply = AsyncMock()
    return message


@pytest.mark.asyncio
@pytest.mark.parametrize("handler_name,arg,expected", [
    ("handle_start", "client", "start"),
    # ("handle_help", "client", "help"),
    ("handle_audio", "client", "audio"),
    ("handle_document", "client", "documents"),
    ("handle_photo", "client", "photo"),
    ("handle_sticker", "client", "sticker"),
    ("handle_video", "client", "video"),
    ("handle_text", "client", "text"),
])
async def test_handlers_reply_expected_message(mock_client, message_mock, handler_name, arg, expected):
    handler = MessageHandler(mock_client)
    method = getattr(handler, handler_name)
    await method(arg, message_mock)
    message_mock.reply.assert_awaited_once_with(
        MessageHandler.DEFAULT_RESPONSE.format(expected)
    )


def test_setup_handlers_calls_on_message(mock_client):
    MessageHandler(mock_client)

    assert mock_client.on_message.call_count == 8
