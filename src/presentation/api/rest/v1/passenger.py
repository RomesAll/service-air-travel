from src.application.dtos import PassengerDtoGet, PassengerDtoPost, PassengerDtoUpdate
from src.application.services import PassengerService
from src.infrastructures.db.repositories import PassengerRepository
from fastapi import APIRouter

router = APIRouter(prefix='/passenger', tags=['Passenger'])

@router.get('/', response_model=list[PassengerDtoGet])
def get_all_passengers():
    result = PassengerService(PassengerRepository).get_all_passenger()
    return result

@router.get('/{passenger_id}', response_model=PassengerDtoGet)
def get_passenger_by_id(passenger_id: int):
    result = PassengerService(PassengerRepository).get_passenger_by_id(passenger_id)
    return result

@router.post('/', response_model=PassengerDtoGet)
def create_passenger(passenger_dto: PassengerDtoPost):
    result = PassengerService(PassengerRepository).add_passenger(passenger_dto)
    return result

@router.put('/{passenger_id}', response_model=PassengerDtoGet)
def update_passenger(passenger_id: int, passenger_dto: PassengerDtoUpdate):
    result = PassengerService(PassengerRepository).update_passenger(passenger_id, passenger_dto)
    return result

@router.delete('/{passenger_id}', response_model=PassengerDtoGet)
def delete_passenger(passenger_id: int):
    result = PassengerService(PassengerRepository).delete_passenger(passenger_id)
    return result
