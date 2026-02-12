from pydantic import BaseModel, Field
from src.domain.entities import PassengerId, TripId

class PassInTripDtoPost(BaseModel):
    trip: TripId
    passenger: PassengerId
    place: str

class PassInTripDtoGet(PassInTripDtoPost):
    id: int

class PassInTripDtoUpdate(BaseModel):
    trip: TripId = Field(default=None)
    passenger: PassengerId = Field(default=None)
    place: str = Field(default=None)