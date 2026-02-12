from src.application.dtos import PassInTripDtoGet, PassInTripDtoPost, PassInTripDtoUpdate
from src.application.services import PassInTripService
from src.infrastructures.db.repositories import PassInTripRepository
from fastapi import APIRouter

router = APIRouter(prefix='/pass-in-trip', tags=['Pass in trip'])

@router.get('/', response_model=list[PassInTripDtoGet])
def get_all_pass_in_trip():
    result = PassInTripService(PassInTripRepository).get_all_pass_in_trip()
    return result

@router.get('/{pass_in_trip_id}', response_model=PassInTripDtoGet)
def get_pass_in_trip_by_id(pass_in_trip_id: int):
    result = PassInTripService(PassInTripRepository).get_pass_in_trip_by_id(pass_in_trip_id)
    return result

@router.post('/', response_model=PassInTripDtoGet)
def create_pass_in_trip(pass_in_trip_dto: PassInTripDtoPost):
    result = PassInTripService(PassInTripRepository).add_pass_in_trip(pass_in_trip_dto)
    return result

@router.put('/{pass_in_trip_id}', response_model=PassInTripDtoGet)
def update_pass_in_trip(pass_in_trip_id: int, pass_in_trip_dto: PassInTripDtoUpdate):
    result = PassInTripService(PassInTripRepository).update_pass_in_trip(pass_in_trip_id, pass_in_trip_dto)
    return result

@router.delete('/{pass_in_trip_id}', response_model=PassInTripDtoGet)
def delete_pass_in_trip(pass_in_trip_id: int):
    result = PassInTripService(PassInTripRepository).delete_pass_in_trip(pass_in_trip_id)
    return result
