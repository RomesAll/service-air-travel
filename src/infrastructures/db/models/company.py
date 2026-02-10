from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Company(Base):
    name: Mapped[str] = mapped_column(unique=True)