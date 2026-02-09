from datetime import datetime
from dataclasses import dataclass
from typing import final
from typing import NewType
from ..value_objects import Town

CompanyId = NewType("CompanyId", int)

@final
@dataclass(frozen=True, kw_only=True, slots=True)
class TripEntities:
    id: int
    company: CompanyId
    plane: str
    town_from: Town
    town_to: Town
    time_out: datetime
    time_in: datetime