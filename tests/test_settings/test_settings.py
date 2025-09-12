import importlib
import sys
from unittest.mock import patch

import pytest

@pytest.mark.parametrize(
    "env_key,env_value",
    [
        ("BOT_NAME", "MeuBot"),
        ("TELEGRAM_API_ID", "12345"),
        ("TELEGRAM_API_HASH", "hashvalue"),
        ("TELEGRAM_BOT_TOKEN", "token_bot"),
    ]
)
def test_env_loaded_for_each_setting(env_key, env_value):
    module_name = "src.settings"
    if module_name in sys.modules:
        del sys.modules[module_name]
    with patch.dict("os.environ", {env_key: env_value}):
        imported = importlib.import_module(module_name)
        assert getattr(imported, env_key) == env_value

def test_all_settings_loaded():
    env_vars = {
        "BOT_NAME": "BotTest",
        "TELEGRAM_API_ID": "idTeste",
        "TELEGRAM_API_HASH": "hashTeste",
        "TELEGRAM_BOT_TOKEN": "tokenTeste",
    }
    module_name = "src.settings"
    if module_name in sys.modules:
        del sys.modules[module_name]
    with patch.dict("os.environ", env_vars):
        imported = importlib.import_module(module_name)
        assert imported.BOT_NAME == "BotTest"
        assert imported.TELEGRAM_API_ID == "idTeste"
        assert imported.TELEGRAM_API_HASH == "hashTeste"
        assert imported.TELEGRAM_BOT_TOKEN == "tokenTeste"