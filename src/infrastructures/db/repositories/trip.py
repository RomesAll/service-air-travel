from .repository import SqlAlchemyRepository
from src.infrastructures.db.models.trip import Trip
from src.infrastructures.db.mappers.trip import TripMapperOrm

class TripRepository(SqlAlchemyRepository):
    model = Trip
    mapper = TripMapperOrm