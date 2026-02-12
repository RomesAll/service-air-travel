from src.application.dtos import TripDtoGet, TripDtoPost, TripDtoUpdate
from src.application.interfases.repositories import IRepository
from src.domain.entities import TripEntities
from src.infrastructures.mappers.trip import TripMapperDto

class TripService:
    def __init__(self, repository):
        self.repository: IRepository = repository()

    def get_trip_by_id(self, trip_id: int) -> TripDtoGet:
        result: TripEntities = self.repository.get_by_id(id=trip_id)
        dto_model: TripDtoGet = TripMapperDto.to_dto(result)
        return dto_model

    def get_all_trip(self) -> list[TripDtoGet]:
        results: list[TripEntities] = self.repository.get_all()
        dto_models: list[TripDtoGet] = [TripMapperDto.to_dto(row) for row in results]
        return dto_models

    def add_trip(self, trip_dto: TripDtoPost) -> TripDtoGet:
        new_object = TripMapperDto.to_dict(trip_dto)
        result: TripEntities = self.repository.add(new_object=new_object)
        dto_model: TripDtoGet = TripMapperDto.to_dto(result)
        return dto_model

    def update_trip(self, trip_id: int, trip_dto: TripDtoUpdate) -> TripDtoGet:
        update_object = TripMapperDto.to_dict(trip_dto)
        result: TripEntities = self.repository.update(id=trip_id, update_obj=update_object)
        dto_model: TripDtoGet = TripMapperDto.to_dto(result)
        return dto_model

    def delete_trip(self, trip_id: int) -> TripDtoGet:
        result: TripEntities = self.repository.delete(id=trip_id)
        dto_model: TripDtoGet = TripMapperDto.to_dto(result)
        return dto_model