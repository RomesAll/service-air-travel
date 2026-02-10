from pydantic import BaseModel

class TownDto(BaseModel):
    name: str
    utc: str
    airport: str