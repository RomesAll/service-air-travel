from .repository import SqlAlchemyRepository
from src.infrastructures.db.models.company import Company
from src.infrastructures.db.mappers.company import CompanyMapperOrm

class CompanyRepository(SqlAlchemyRepository):
    model = Company
    mapper = CompanyMapperOrm