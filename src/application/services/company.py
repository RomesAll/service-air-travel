from src.application.dtos import CompanyDtoPost, CompanyDtoUpdate, CompanyDtoGet
from src.application.interfases.repositories import IRepository
from src.domain.entities import CompanyEntity

class CompanyService:
    def __init__(self, repository):
        self.repository: IRepository = repository

    def get_company_by_id(self, company_id: int) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.get_by_id(company_id)
        dto_model: CompanyDtoGet = CompanyDtoGet(id=result.id, name=result.name)
        return dto_model

    def get_all_company(self) -> list[CompanyDtoGet]:
        results: list[CompanyEntity] = self.repository.get_all()
        dto_models: list[CompanyDtoGet] = [CompanyDtoGet(id=row.id, name=row.name) for row in results]
        return dto_models

    def add_company(self, company_dto: CompanyDtoPost) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.add(company_dto)
        dto_model: CompanyDtoGet = CompanyDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model

    def update_company(self, company_id: int, company_dto: CompanyDtoUpdate) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.update(company_id, company_dto)
        dto_model: CompanyDtoGet = CompanyDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model

    def delete_company(self, company_id: int) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.delete(company_id)
        dto_model: CompanyDtoGet = CompanyDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model