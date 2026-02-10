from src.application.dtos import TripDtoGet, TripDtoPost, TripDtoUpdate
from src.application.interfases.repositories import IRepository
from src.domain.entities import TripEntities

class TripService:
    def __init__(self, repository):
        self.repository: IRepository = repository

    def get_trip_by_id(self, trip_id: int) -> TripDtoGet:
        result: TripEntities = self.repository.get_by_id(trip_id)
        dto_model: TripDtoGet = TripDtoGet(
            id=result.id,
            company=result.company,
            plane=result.plane,
            town_from=result.town_from,
            town_to=result.town_to,
            time_out=result.time_out,
            time_in=result.time_in,
        )
        return dto_model

    def get_all_trip(self) -> list[TripDtoGet]:
        results: list[TripEntities] = self.repository.get_all()
        dto_models: list[TripDtoGet] = [TripDtoGet(
            id=row.id,
            company=row.company,
            plane=row.plane,
            town_from=row.town_from,
            town_to=row.town_to,
            time_out=row.time_out,
            time_in=row.time_in,
        ) for row in results]
        return dto_models

    def add_trip(self, trip_dto: TripDtoPost) -> TripDtoGet:
        result: TripEntities = self.repository.add(trip_dto)
        dto_model: TripDtoGet = TripDtoGet(
            id=result.id,
            company=result.company,
            plane=result.plane,
            town_from=result.town_from,
            town_to=result.town_to,
            time_out=result.time_out,
            time_in=result.time_in,
        )
        self.repository.commit()
        return dto_model

    def update_trip(self, trip_id: int, trip_dto: TripDtoUpdate) -> TripDtoGet:
        result: TripEntities = self.repository.update(trip_id, trip_dto)
        dto_model: TripDtoGet = TripDtoGet(
            id=result.id,
            company=result.company,
            plane=result.plane,
            town_from=result.town_from,
            town_to=result.town_to,
            time_out=result.time_out,
            time_in=result.time_in,
        )
        self.repository.commit()
        return dto_model

    def delete_trip(self, trip_id: int) -> TripDtoGet:
        result: TripEntities = self.repository.delete(trip_id)
        dto_model: TripDtoGet = TripDtoGet(
            id=result.id,
            company=result.company,
            plane=result.plane,
            town_from=result.town_from,
            town_to=result.town_to,
            time_out=result.time_out,
            time_in=result.time_in,
        )
        self.repository.commit()
        return dto_model