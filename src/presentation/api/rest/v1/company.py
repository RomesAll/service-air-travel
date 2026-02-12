from src.application.dtos import CompanyDtoGet, CompanyDtoPost, CompanyDtoUpdate
from src.application.services import CompanyService
from src.infrastructures.db.repositories import CompanyRepository
from fastapi import APIRouter

router = APIRouter(prefix='/company', tags=['Company'])

@router.get('/', response_model=list[CompanyDtoGet])
def get_all_companies():
    result = CompanyService(CompanyRepository).get_all_company()
    return result

@router.get('/{company_id}', response_model=CompanyDtoGet)
def get_company_by_id(company_id: int):
    result = CompanyService(CompanyRepository).get_company_by_id(company_id)
    return result

@router.post('/', response_model=CompanyDtoGet)
def create_company(company_dto: CompanyDtoPost):
    result = CompanyService(CompanyRepository).add_company(company_dto)
    return result

@router.put('/{company_id}', response_model=CompanyDtoGet)
def update_company(company_id: int, company_dto: CompanyDtoUpdate):
    result = CompanyService(CompanyRepository).update_company(company_id, company_dto)
    return result

@router.delete('/{company_id}', response_model=CompanyDtoGet)
def delete_company(company_id: int):
    result = CompanyService(CompanyRepository).delete_company(company_id)
    return result
