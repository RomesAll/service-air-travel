from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.config import settings
from typing import Final

engine: Final = create_engine(settings.postgres.get_postgres_url_sync)

session_factory: Final = sessionmaker(bind=engine,
                               expire_on_commit=False,
                               autoflush=False,
                               autocommit=False)