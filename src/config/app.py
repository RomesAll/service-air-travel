from .base import BaseConfig
from typing import Literal

class AppConfig(BaseConfig):
    APP_NAME: str|None = None
    ENV_TYPE: Literal['local', 'debug', 'test']|None = None
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']|None = None
    DEBUG: bool|None = None