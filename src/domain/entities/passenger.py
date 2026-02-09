from dataclasses import dataclass
from typing import final
from ..exceptions import DomainValidationError

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PassengerEntities:
    id: int
    name: str

    def __post_init__(self):
        if not(self.name and len(self.name) >= 2):
            raise DomainValidationError(f"Name passenger cannot be none or incorrect, name: {self.name}")