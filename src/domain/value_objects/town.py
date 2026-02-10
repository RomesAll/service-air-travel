from dataclasses import dataclass
from ..exceptions import InvalidTownError
import re

@dataclass(frozen=True, order=True, kw_only=True, slots=True)
class Town:
    __separation: str = '-'
    name: str
    utc: str
    airport: str

    def __post_init__(self):
        if not(self.name and len(self.name) >= 2):
            raise InvalidTownError(f"Name cannot be none or incorrect, name: {self.name}")
        if re.fullmatch(r'UTC\+\d+', self.utc) is None:
            raise InvalidTownError(f"Time is invalid, utc: {self.utc}")
        if not(self.airport and len(self.airport) >= 2):
            raise InvalidTownError(f"Airport cannot be none or incorrect, airport: {self.airport}")

    @property
    def separation(self) -> str:
        return Town.__separation

    @separation.setter
    def separation(self, value):
        Town.__separation = value

    def get_town_info(self):
        return f'{Town.__separation}'.join([self.name, self.utc, self.airport])