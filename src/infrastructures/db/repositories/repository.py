from collections.abc import Callable
from sqlalchemy.sql.annotation import Annotated
from src.application.interfases.repositories import IRepository
from src.domain import UnionEntity
from sqlalchemy import select, insert, update, delete
from src.application.interfases.mappers_orm import MapperOrm
from src.infrastructures.db.models import Base
from ..database import session_factory
from ..exceptions import MappersNoneException, RecordsNoneException, RecordsNoFoundException

class SqlAlchemyRepository(IRepository):
    model: Annotated[Base, Callable] = Base
    mapper: MapperOrm = MapperOrm

    def get_all(self) -> list[UnionEntity]:
        with session_factory() as session:
            stmt = select(self.model)
            results = session.execute(stmt).scalars().all()
            if results is None:
                raise RecordsNoneException('Records is not defined')
            if self.mapper is None:
                raise MappersNoneException('Mapper is not defined')
            entity_list = [self.mapper.to_entity(result) for result in results]
            return entity_list

    def get_by_id(self, *, id: int) -> UnionEntity:
        with session_factory() as session:
            stmt = select(self.model).filter_by(id=id)
            result = session.execute(stmt).scalar_one_or_none()
            if result is None:
                raise RecordsNoneException('Records is not defined')
            if self.mapper is None:
                raise MappersNoneException('Mapper is not defined')
            entity_list = self.mapper.to_entity(result)
            return entity_list

    def add(self, *, new_object: dict) -> UnionEntity:
        with session_factory() as session:
            stmt = (insert(self.model)
                    .values(**new_object)
                    .returning(self.model.id))
            result = session.execute(stmt).scalar_one()
            if result is None:
                raise RecordsNoneException('Records is not append')
            if self.mapper is None:
                raise MappersNoneException('Mapper is not defined')
            orm_object = self.model(id=result, **new_object)
            entity = self.mapper.to_entity(orm_object)
            session.commit()
            return entity

    def update(self, *, id: int, update_obj: dict) -> UnionEntity:
        with session_factory() as session:
            update_object = select(self.model).where(self.model.id == id)
            old_orm_object = session.execute(update_object).scalar_one_or_none()
            if old_orm_object is None:
                raise RecordsNoFoundException('Record not found')
            stmt = (update(self.model)
                    .where(self.model.id == id)
                    .values(**update_obj)
                    .returning(self.model.id))
            result = session.execute(stmt).scalar_one()
            if result is None:
                raise RecordsNoneException('Records is not updating')
            if self.mapper is None:
                raise MappersNoneException('Mapper is not defined')
            orm_object = self.model(**{**old_orm_object.get_attrs(), **update_obj})
            entity = self.mapper.to_entity(orm_object)
            session.commit()
            return entity

    def delete(self, *, id: int) -> UnionEntity:
        with session_factory() as session:
            delete_object = select(self.model).where(self.model.id == id)
            orm_object = session.execute(delete_object).scalar_one_or_none()
            if orm_object is None:
                raise RecordsNoFoundException('Record not found')
            stmt = delete(self.model).where(self.model.id == id).returning(self.model.id)
            result = session.execute(stmt).scalar_one()
            if result is None:
                raise RecordsNoneException('Records is not updating')
            if self.mapper is None:
                raise MappersNoneException('Mapper is not defined')
            entity = self.mapper.to_entity(orm_object)
            return entity