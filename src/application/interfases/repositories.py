from abc import ABC, abstractmethod
from typing import List
from src.domain.entities import UnionEntity

class IRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UnionEntity] | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> UnionEntity | None:
        raise NotImplementedError

    @abstractmethod
    def add(self, new_object: dict) -> UnionEntity | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, update_obj: dict) -> UnionEntity | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> UnionEntity | None:
        raise NotImplementedError