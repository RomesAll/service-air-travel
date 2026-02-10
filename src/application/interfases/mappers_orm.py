from abc import ABC, abstractmethod
from src.domain.entities import UnionEntity
from src.infrastructures.db.models import Base

class MapperOrm(ABC):
    @abstractmethod
    def to_entity(self, orm_model: Base) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def to_orm_model(self, entity: UnionEntity) -> Base:
        raise NotImplementedError