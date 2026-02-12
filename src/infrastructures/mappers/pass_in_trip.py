from src.application.interfases.mappers_dto import MapperDto
from src.domain import PassInTripEntities
from src.application.dtos import PassInTripDtoGet

class PassInTripMapperDto(MapperDto):

    @classmethod
    def to_entity(cls, dto_model: PassInTripDtoGet) -> PassInTripEntities:
        return PassInTripEntities(
            id=dto_model.id,
            trip=dto_model.trip,
            passenger=dto_model.passenger,
            place=dto_model.place,
        )

    @classmethod
    def to_dto(cls, entity: PassInTripEntities) -> PassInTripDtoGet:
        return PassInTripDtoGet(
            id=entity.id,
            trip=entity.trip,
            passenger=entity.passenger,
            place=entity.place,
        )