from pydantic import BaseModel, Field
from src.domain.entities import CompanyId
from datetime import datetime
from src.domain.value_objects import Town
from src.domain.value_objects.town import SEPARATION

class TownDto(BaseModel):
    separation: str = Field(default=SEPARATION, exclude=True)
    name: str
    utc: str
    airport: str

class TripDtoPost(BaseModel):
    company: CompanyId
    plane: str
    town_from: TownDto
    town_to: TownDto
    time_out: datetime
    time_in: datetime

class TripDtoGet(TripDtoPost):
    id: int

class TripDtoUpdate(BaseModel):
    company: CompanyId = Field(default=None)
    plane: str = Field(default=None)
    town_from: TownDto = Field(default=None)
    town_to: TownDto = Field(default=None)
    time_out: datetime = Field(default=None)
    time_in: datetime = Field(default=None)