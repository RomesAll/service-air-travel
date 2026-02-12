from src.application.interfases.mappers_dto import MapperDto
from src.domain import CompanyEntity
from src.application.dtos import CompanyDtoGet

class CompanyMapperDto(MapperDto):

    @classmethod
    def to_entity(cls, dto_model: CompanyDtoGet) -> CompanyEntity:
        return CompanyEntity(
            id=dto_model.id,
            name=dto_model.name,
        )

    @classmethod
    def to_dto(cls, entity: CompanyEntity) -> CompanyDtoGet:
        return CompanyDtoGet(
            id=entity.id,
            name=entity.name,
        )