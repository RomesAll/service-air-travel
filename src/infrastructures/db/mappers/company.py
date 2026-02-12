from src.application.interfases.mappers_orm import MapperOrm
from src.domain import CompanyEntity
from src.infrastructures.db.models import Company

class CompanyMapperOrm(MapperOrm):

    @classmethod
    def to_entity(cls, orm_model: Company) -> CompanyEntity:
        return CompanyEntity(
            id=orm_model.id,
            name=orm_model.name,
        )

    @classmethod
    def to_orm_model(cls, entity: CompanyEntity) -> Company:
        return Company(
            id=entity.id,
            name=entity.name,
        )