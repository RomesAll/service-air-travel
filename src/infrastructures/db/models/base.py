from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData()
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @classmethod
    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower()

    def get_attrs(self) -> dict:
        columns = self.__table__.columns.keys()
        dict_attrs = {column: getattr(self, column) for column in columns}
        return dict_attrs