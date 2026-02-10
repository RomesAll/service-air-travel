from src.application.dtos import UnionUpdateDto, UnionPostDto
from src.application.interfases.repositories import IRepository
from src.domain import UnionEntity
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update
from src.application.interfases.mappers_orm import MapperOrm
from src.infrastructures.db.models import Base
from ..exceptions import MappersNoneException

class SqlAlchemyRepository(IRepository):
    model: Base = None
    mapper: MapperOrm = None

    def __init__(self, session):
        self._session: Session = session

    def get_all(self):
        stmt = select(self.model)
        results = self._session.execute(stmt).scalars().all()
        if results is None:
            return None
        if self.mapper is None:
            raise MappersNoneException('Mapper is not defined')
        entity_list = [self.mapper.to_entity(result) for result in results]
        return entity_list

    def get_by_id(self, id: int):
        stmt = select(self.model).filter_by(id=id)
        result = self._session.execute(stmt).scalar_one_or_none()
        if result is None:
            return None
        if self.mapper is None:
            raise MappersNoneException('Mapper is not defined')
        entity_list = self.mapper.to_entity(result)
        return entity_list

    def add(self, new_object: UnionPostDto):
        stmt = (insert(self.model)
                .values(**new_object.model_dump(exclude_none=True))
                .returning(self.model.id))
        result = self._session.execute(stmt)
        if result is None:
            return None
        if self.mapper is None:
            raise MappersNoneException('Mapper is not defined')
        orm_object = self.model(id=result, **new_object.model_dump(exclude_none=True))
        entity = self.mapper.to_entity(orm_object)
        return entity

    def update(self, id: int, update_obj: UnionUpdateDto) -> UnionEntity:
        stmt = (update(self.model)
                .where(self.model.id == id)
                .value(**update_obj.model_dump(exclude_none=True))
                .returning(self.model.id))
        result = self._session.execute(stmt)
        if result is None:
            return None
        if self.mapper is None:
            raise MappersNoneException('Mapper is not defined')
        orm_object = self.model(id=result, **update_obj.model_dump(exclude_none=True))
        entity = self.mapper.to_entity(orm_object)
        return entity