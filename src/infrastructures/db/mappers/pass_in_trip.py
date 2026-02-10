from src.application.interfases.mappers_orm import MapperOrm
from src.domain import PassInTripEntities
from src.infrastructures.db.models import PassInTrip

class PassInTripMapperOrm(MapperOrm):

    def to_entity(self, orm_model: PassInTrip) -> PassInTripEntities:
        return PassInTripEntities(
            id=orm_model.id,
            trip=orm_model.trip,
            passenger=orm_model.passenger,
            place=orm_model.place,
        )

    def to_orm_model(self, entity: PassInTripEntities) -> PassInTrip:
        return PassInTrip(
            id=entity.id,
            trip=entity.trip,
            passenger=entity.passenger,
            place=entity.place,
        )