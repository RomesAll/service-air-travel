from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.domain.entities import TripId, PassengerId

class PassInTrip(Base):
    trip: Mapped[TripId] = mapped_column(ForeignKey('trip.id', ondelete='CASCADE'))
    passenger: Mapped[PassengerId] = mapped_column(ForeignKey('passenger.id', ondelete='CASCADE'))
    place: Mapped[str]