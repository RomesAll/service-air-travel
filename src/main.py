from src.infrastructures.db.repositories.trip import TripRepository
from src.infrastructures.db.database import session_factory
from src.application.services.trip import TripService
from src.application.dtos import TripDtoPost, TripDtoUpdate
from src.application.dtos.trip import TownDto
from src.domain.value_objects import Town
from datetime import datetime

res = TripService(TripRepository).update_trip(trip_id=13, trip_dto=TripDtoUpdate(
    plane='Tu-3227',
))
print(res)
