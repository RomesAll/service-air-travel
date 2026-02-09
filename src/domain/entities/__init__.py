from .trip import TripEntities, CompanyId
from .pass_in_trip import PassInTripEntities, TripId, PassengerId
from .passenger import PassengerEntities
from .company import CompanyEntity
from typing import Union

UnionEntity = Union[CompanyEntity, TripEntities, PassengerEntities, PassInTripEntities]

__all__ = (
    'TripEntities',
    'PassInTripEntities',
    'PassengerEntities',
    'CompanyEntity',
    'UnionEntity',
    'TripId',
    'PassengerId',
    'CompanyId'
)