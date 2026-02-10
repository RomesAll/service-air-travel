from src.application.interfases.mappers_orm import MapperOrm
from src.domain import TripEntities, Town
from src.infrastructures.db.models import Trip

class TripMapperOrm(MapperOrm):

    def to_entity(self, orm_model: Trip) -> TripEntities:
        town_from_info = orm_model.town_from.split(str(Town.separation))
        town_to_info = orm_model.town_to.split(str(Town.separation))
        return TripEntities(
            id=orm_model.id,
            company=orm_model.company,
            plane=orm_model.plane,
            town_from=Town(name=town_from_info[0], utc=town_from_info[1], airport=town_from_info[2]),
            town_to=Town(name=town_to_info[0], utc=town_to_info[1], airport=town_to_info[2]),
            time_out=orm_model.time_out,
            time_in=orm_model.time_in,
        )

    def to_orm_model(self, entity: TripEntities) -> Trip:
        return Trip(
            id=entity.id,
            company=entity.company,
            plane=entity.plane,
            town_from=entity.town_from.get_town_info(),
            town_to=entity.town_to.get_town_info(),
            time_out=entity.time_out,
            time_in=entity.time_in,
        )
