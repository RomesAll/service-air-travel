from .repository import SqlAlchemyRepository
from src.infrastructures.db.models.pass_in_trip import PassInTrip
from src.infrastructures.db.mappers.pass_in_trip import PassInTripMapperOrm

class PassInTripRepository(SqlAlchemyRepository):
    model = PassInTrip
    mapper = PassInTripMapperOrm