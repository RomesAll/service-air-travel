from abc import ABC, abstractmethod
from typing import List
from src.domain.entities import UnionEntity
from ..dtos import UnionPostDto, UnionUpdateDto

class IRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UnionEntity] | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> UnionEntity | None:
        raise NotImplementedError

    @abstractmethod
    def add(self, new_object: UnionPostDto) -> UnionEntity | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, update_obj: UnionUpdateDto) -> UnionEntity | None:
        raise NotImplementedError