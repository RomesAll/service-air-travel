from src.application.dtos import CompanyDtoPost, CompanyDtoUpdate, CompanyDtoGet
from src.application.interfases.repositories import IRepository
from src.domain.entities import CompanyEntity
from src.infrastructures.mappers.company import CompanyMapperDto

class CompanyService:
    def __init__(self, repository):
        self.repository: IRepository = repository()

    def get_company_by_id(self, company_id: int) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.get_by_id(id=company_id)
        dto_model: CompanyDtoGet = CompanyMapperDto.to_dto(result)
        return dto_model

    def get_all_company(self) -> list[CompanyDtoGet]:
        results: list[CompanyEntity] = self.repository.get_all()
        dto_models: list[CompanyDtoGet] = [CompanyMapperDto.to_dto(row) for row in results]
        return dto_models

    def add_company(self, company_dto: CompanyDtoPost) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.add(new_object=company_dto.model_dump(exclude_none=True))
        dto_model: CompanyDtoGet = CompanyMapperDto.to_dto(result)
        return dto_model

    def update_company(self, company_id: int, company_dto: CompanyDtoUpdate) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.update(id=company_id,
                                                       update_obj=company_dto.model_dump(exclude_none=True))
        dto_model: CompanyDtoGet = CompanyMapperDto.to_dto(result)
        return dto_model

    def delete_company(self, company_id: int) -> CompanyDtoGet:
        result: CompanyEntity = self.repository.delete(id=company_id)
        dto_model: CompanyDtoGet = CompanyMapperDto.to_dto(result)
        return dto_model