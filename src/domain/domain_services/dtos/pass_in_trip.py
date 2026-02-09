from pydantic import BaseModel
from src.domain.entities import PassengerId, TripId

class PassInTripDtoPost(BaseModel):
    trip: TripId
    passenger: PassengerId
    place: str

class PassInTripDtoGet(PassInTripDtoPost):
    id: int

class PassInTripDtoUpdate(PassInTripDtoPost):
    pass