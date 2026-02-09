from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

APP_DIR = Path(__file__).parent.parent
BASE_DIR = APP_DIR.parent

class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{BASE_DIR}/.env',
                                      extra='ignore',
                                      env_file_encoding='utf-8')