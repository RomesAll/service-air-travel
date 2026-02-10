from src.application.interfases.mappers_orm import MapperOrm
from src.domain import PassengerEntities
from src.infrastructures.db.models import Passenger

class PassengerMapperOrm(MapperOrm):

    def to_entity(self, orm_model: Passenger) -> PassengerEntities:
        return PassengerEntities(
            id=orm_model.id,
            name=orm_model.name,
        )

    def to_orm_model(self, entity: PassengerEntities) -> Passenger:
        return Passenger(
            id=entity.id,
            name=entity.name,
        )