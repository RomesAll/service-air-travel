from src.application.interfases.mappers_dto import MapperDto
from src.domain import TripEntities, Town
from src.application.dtos import TripDtoGet, TripDtoPost
from src.application.dtos.trip import TownDto

class TripMapperDto(MapperDto):

    @classmethod
    def to_entity(cls, dto_model: TripDtoGet) -> TripEntities:
        town_from_info = dto_model.town_from
        town_to_info = dto_model.town_to
        return TripEntities(
            id=dto_model.id,
            company=dto_model.company,
            plane=dto_model.plane,
            town_from=Town(name=town_from_info.name,
                           utc=town_from_info.utc,
                           airport=town_from_info.airport),
            town_to=Town(name=town_to_info.name,
                         utc=town_to_info.utc,
                         airport=town_to_info.airport),
            time_out=dto_model.time_out,
            time_in=dto_model.time_in,
        )

    @classmethod
    def to_dto(cls, entity: TripEntities) -> TripDtoGet:
        return TripDtoGet(
            id=entity.id,
            company=entity.company,
            plane=entity.plane,
            town_from=TownDto(separation=entity.town_from.separation,
                              name=entity.town_from.name,
                              utc=entity.town_from.utc,
                              airport=entity.town_from.airport),
            town_to=TownDto(separation=entity.town_to.separation,
                              name=entity.town_to.name,
                              utc=entity.town_to.utc,
                              airport=entity.town_to.airport),
            time_out=entity.time_out,
            time_in=entity.time_in,
        )

    @classmethod
    def to_dict(cls, dto_model):
        object_dict = dto_model.model_dump(exclude_none=True, exclude=['town_from', 'town_to'])
        if dto_model.town_from is not None:
            object_dict['town_from'] = Town(separation=dto_model.town_from.separation,
                                            name=dto_model.town_from.name,
                                            utc=dto_model.town_from.utc,
                                            airport=dto_model.town_from.airport).get_town_info()
        if dto_model.town_to is not None:
            object_dict['town_to'] = Town(separation=dto_model.town_to.separation,
                                            name=dto_model.town_to.name,
                                            utc=dto_model.town_to.utc,
                                            airport=dto_model.town_to.airport).get_town_info()
        return object_dict