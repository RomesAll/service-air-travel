from datetime import datetime
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.domain.entities import CompanyId

class Trip(Base):
    company: Mapped[CompanyId] = mapped_column(ForeignKey('company.id', ondelete='CASCADE'))
    plane: Mapped[str]
    town_from: Mapped[str]
    town_to: Mapped[str]
    time_out: Mapped[datetime]
    time_in: Mapped[datetime]