from .company import *
from .pass_in_trip import *
from .trip import *
from .passenger import *
from typing import Union

UnionPostDto = Union[
    CompanyDtoPost,
    PassInTripDtoPost,
    PassengerDtoPost,
    TripDtoPost,
]

UnionUpdateDto = Union[
    CompanyDtoUpdate,
    PassInTripDtoUpdate,
    PassengerDtoUpdate,
    TripDtoUpdate,
]

UnionDto = Union[
    CompanyDtoGet,
    PassInTripDtoGet,
    PassengerDtoGet,
    TripDtoGet
]

__all__ = (
    'CompanyDtoPost',
    'CompanyDtoGet',
    'CompanyDtoUpdate',
    'PassInTripDtoPost',
    'PassInTripDtoGet',
    'PassInTripDtoUpdate',
    'PassengerDtoPost',
    'PassengerDtoGet',
    'PassengerDtoUpdate',
    'TripDtoPost',
    'TripDtoGet',
    'TripDtoUpdate',
    'UnionPostDto',
    'UnionUpdateDto',
    'UnionDto'
)