from src.application.dtos import PassengerDtoGet, PassengerDtoUpdate, PassengerDtoPost
from src.application.interfases.repositories import IRepository
from src.domain.entities import PassengerEntities

class PassengerService:
    def __init__(self, repository):
        self.repository: IRepository = repository

    def get_passenger_by_id(self, passenger_id: int) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.get_by_id(passenger_id)
        dto_model: PassengerDtoGet = PassengerDtoGet(id=result.id, name=result.name)
        return dto_model

    def get_all_passenger(self) -> list[PassengerDtoGet]:
        results: list[PassengerEntities] = self.repository.get_all()
        dto_models: list[PassengerDtoGet] = [PassengerDtoGet(id=row.id, name=row.name) for row in results]
        return dto_models

    def add_passenger(self, passenger_dto: PassengerDtoPost) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.add(passenger_dto)
        dto_model: PassengerDtoGet = PassengerDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model

    def update_passenger(self, passenger_id: int, passenger_dto: PassengerDtoUpdate) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.update(passenger_id, passenger_dto)
        dto_model: PassengerDtoGet = PassengerDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model

    def delete_passenger(self, passenger_id: int) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.delete(passenger_id)
        dto_model: PassengerDtoGet = PassengerDtoGet(id=result.id, name=result.name)
        self.repository.commit()
        return dto_model