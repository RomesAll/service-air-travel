from pydantic import BaseModel

class CompanyDtoPost(BaseModel):
    name: str

class CompanyDtoGet(CompanyDtoPost):
    id: int

class CompanyDtoUpdate(CompanyDtoPost):
    pass