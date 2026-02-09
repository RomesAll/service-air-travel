from src.dependency.decorators import checking_var_db
from .base import BaseConfig

class PostgresSettings(BaseConfig):
    POSTGRES_HOST: str|None = None
    POSTGRES_PORT: int|None = None
    POSTGRES_USER: str|None = None
    POSTGRES_PASS: str|None = None
    POSTGRES_DB: str|None = None

    @property
    @checking_var_db
    def get_postgres_url_sync(self) -> str:
        return (f'postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}'
                f'@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}')

    @property
    def get_postgres_url_default(self) ->str:
        return f'sqlite+pysqlite:///:default.db:'

    def get_attrs(self) ->dict:
        return self.__dict__

    def is_empty(self) -> bool:
        return any([v is None for k, v in self.get_attrs().items()])