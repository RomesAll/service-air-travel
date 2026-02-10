from abc import ABC, abstractmethod
from src.domain.entities import UnionEntity
from src.application.dtos import UnionDto

class MapperDto(ABC):
    @abstractmethod
    def to_entity(self, dto_model: UnionDto) -> UnionEntity:
        raise NotImplementedError

    @abstractmethod
    def to_dto(self, entity: UnionEntity) -> UnionDto:
        raise NotImplementedError