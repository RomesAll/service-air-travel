from .repository import SqlAlchemyRepository
from src.infrastructures.db.models.passenger import Passenger
from src.infrastructures.db.mappers.passenger import PassengerMapperOrm

class PassengerRepository(SqlAlchemyRepository):
    model = Passenger
    mapper = PassengerMapperOrm