from pydantic import BaseModel
from src.domain.value_objects import Town
from src.domain.entities import CompanyId
from datetime import datetime

class TripDtoPost(BaseModel):
    company: CompanyId
    plane: str
    town_from: Town
    town_to: Town
    time_out: datetime
    time_in: datetime

class TripDtoGet(TripDtoPost):
    id: int

class TripDtoUpdate(TripDtoPost):
    pass