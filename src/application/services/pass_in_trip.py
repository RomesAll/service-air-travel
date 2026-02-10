from src.application.dtos import PassInTripDtoGet, PassInTripDtoUpdate, PassInTripDtoPost
from src.application.interfases.repositories import IRepository
from src.domain.entities import PassInTripEntities

class PassInTripService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def get_pass_in_trip_by_id(self, pass_in_trip_id: int) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.get_by_id(pass_in_trip_id)
        dto_model: PassInTripDtoGet = PassInTripDtoGet(
            id=result.id,
            trip=result.trip,
            passenger=result.passenger,
            place=result.place
        )
        return dto_model

    def get_all_pass_in_trip(self) -> list[PassInTripDtoGet]:
        results: list[PassInTripEntities] = self.repository.get_all()
        dto_models: list[PassInTripDtoGet] = [PassInTripDtoGet(
            id=row.id,
            trip=row.trip,
            passenger=row.passenger,
            place=row.place
        ) for row in results]
        return dto_models

    def add_pass_in_trip(self, pass_in_trip_dto: PassInTripDtoPost) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.add(pass_in_trip_dto)
        dto_model: PassInTripDtoGet = PassInTripDtoGet(
            id=result.id,
            trip=result.trip,
            passenger=result.passenger,
            place=result.place
        )
        self.repository.commit()
        return dto_model

    def update_pass_in_trip(self, pass_in_trip_id: int, pass_in_trip_dto: PassInTripDtoUpdate) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.update(pass_in_trip_id, pass_in_trip_dto)
        dto_model: PassInTripDtoGet = PassInTripDtoGet(
            id=result.id,
            trip=result.trip,
            passenger=result.passenger,
            place=result.place
        )
        self.repository.commit()
        return dto_model

    def delete_pass_in_trip(self, pass_in_trip_id: int) -> PassInTripDtoGet:
        result: PassInTripEntities = self.repository.delete(pass_in_trip_id)
        dto_model: PassInTripDtoGet = PassInTripDtoGet(
            id=result.id,
            trip=result.trip,
            passenger=result.passenger,
            place=result.place
        )
        self.repository.commit()
        return dto_model