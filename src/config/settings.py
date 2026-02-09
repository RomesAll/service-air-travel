from .database import PostgresSettings
from .app import AppConfig
from pydantic_settings import BaseSettings
from typing import Final

class SettingsConfig(BaseSettings):
    app: AppConfig = AppConfig()
    postgres: PostgresSettings = PostgresSettings()

settings: Final[SettingsConfig] = SettingsConfig()
