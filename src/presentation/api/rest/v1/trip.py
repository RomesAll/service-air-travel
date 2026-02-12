from src.application.dtos import TripDtoPost, TripDtoGet, TripDtoUpdate
from src.application.services import TripService
from src.infrastructures.db.repositories import TripRepository
from fastapi import APIRouter

router = APIRouter(prefix='/trip', tags=['Trip'])

@router.get('/', response_model=list[TripDtoGet])
def get_all_trip():
    result = TripService(TripRepository).get_all_trip()
    return result

@router.get('/{trip_id}', response_model=TripDtoGet)
def get_trip_by_id(trip_id: int):
    result = TripService(TripRepository).get_trip_by_id(trip_id)
    return result

@router.post('/', response_model=TripDtoGet)
def create_trip(trip_dto: TripDtoPost):
    result = TripService(TripRepository).add_trip(trip_dto)
    return result

@router.put('/{trip_id}', response_model=TripDtoGet)
def update_trip(trip_id: int, trip_dto: TripDtoUpdate):
    result = TripService(TripRepository).update_trip(trip_id, trip_dto)
    return result

@router.delete('/{trip_id}', response_model=TripDtoGet)
def delete_trip(trip_id: int):
    result = TripService(TripRepository).delete_trip(trip_id)
    return result
