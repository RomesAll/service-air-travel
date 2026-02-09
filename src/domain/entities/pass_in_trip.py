from typing import NewType
from dataclasses import dataclass
from typing import final

TripId = NewType("TripId", int)
PassengerId = NewType("PassengerId", int)

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PassInTripEntities:
    id: int
    trip: TripId
    passenger: PassengerId
    place: str