from src.application.interfases.mappers_dto import MapperDto
from src.domain import PassengerEntities
from src.application.dtos import PassengerDtoGet

class PassengerMapperDto(MapperDto):

    @classmethod
    def to_entity(cls, dto_model: PassengerDtoGet) -> PassengerEntities:
        return PassengerEntities(
            id=dto_model.id,
            name=dto_model.name,
        )

    @classmethod
    def to_dto(cls, entity: PassengerEntities) -> PassengerDtoGet:
        return PassengerDtoGet(
            id=entity.id,
            name=entity.name,
        )