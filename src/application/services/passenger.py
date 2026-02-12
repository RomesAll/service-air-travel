from src.application.dtos import PassengerDtoGet, PassengerDtoUpdate, PassengerDtoPost
from src.application.interfases.repositories import IRepository
from src.domain.entities import PassengerEntities
from src.infrastructures.mappers.passenger import PassengerMapperDto

class PassengerService:
    def __init__(self, repository):
        self.repository: IRepository = repository()

    def get_passenger_by_id(self, passenger_id: int) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.get_by_id(id=passenger_id)
        dto_model: PassengerDtoGet = PassengerMapperDto.to_dto(result)
        return dto_model

    def get_all_passenger(self) -> list[PassengerDtoGet]:
        results: list[PassengerEntities] = self.repository.get_all()
        dto_models: list[PassengerDtoGet] = [PassengerMapperDto.to_dto(row) for row in results]
        return dto_models

    def add_passenger(self, passenger_dto: PassengerDtoPost) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.add(new_object=passenger_dto.model_dump(exclude_none=True))
        dto_model: PassengerDtoGet = PassengerMapperDto.to_dto(result)
        return dto_model

    def update_passenger(self, passenger_id: int, passenger_dto: PassengerDtoUpdate) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.update(id=passenger_id,
                                                           update_obj=passenger_dto.model_dump(exclude_none=True))
        dto_model: PassengerDtoGet = PassengerMapperDto.to_dto(result)
        return dto_model

    def delete_passenger(self, passenger_id: int) -> PassengerDtoGet:
        result: PassengerEntities = self.repository.delete(id=passenger_id)
        dto_model: PassengerDtoGet = PassengerMapperDto.to_dto(result)
        return dto_model