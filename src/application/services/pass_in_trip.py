from src.application.dtos import PassInTripDtoGet, PassInTripDtoUpdate, PassInTripDtoPost
from src.application.interfases.repositories import IRepository
from src.domain.entities import PassInTripEntities
from src.infrastructures.mappers.pass_in_trip import PassInTripMapperDto

class PassInTripService:
    def __init__(self, repository):
        self.repository: IRepository = repository()

    def get_pass_in_trip_by_id(self, pass_in_trip_id: int) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.get_by_id(id=pass_in_trip_id)
        dto_model: PassInTripDtoGet = PassInTripMapperDto.to_dto(result)
        return dto_model

    def get_all_pass_in_trip(self) -> list[PassInTripDtoGet]:
        results: list[PassInTripEntities] = self.repository.get_all()
        dto_models: list[PassInTripDtoGet] = [PassInTripMapperDto.to_dto(row) for row in results]
        return dto_models

    def add_pass_in_trip(self, pass_in_trip_dto: PassInTripDtoPost) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.add(new_object=pass_in_trip_dto.model_dump(exclude_none=True))
        dto_model: PassInTripDtoGet = PassInTripMapperDto.to_dto(result)
        return dto_model

    def update_pass_in_trip(self, pass_in_trip_id: int, pass_in_trip_dto: PassInTripDtoUpdate) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.update(id=pass_in_trip_id,
                                                            update_obj=pass_in_trip_dto.model_dump(exclude_none=True))
        dto_model: PassInTripDtoGet = PassInTripMapperDto.to_dto(result)
        return dto_model

    def delete_pass_in_trip(self, pass_in_trip_id: int) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.delete(id=pass_in_trip_id)
        dto_model: PassInTripDtoGet = PassInTripMapperDto.to_dto(result)
        return dto_model