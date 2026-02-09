from pydantic import BaseModel

class PassengerDtoPost(BaseModel):
    name: str

class PassengerDtoGet(PassengerDtoPost):
    id: int

class PassengerDtoUpdate(PassengerDtoPost):
    pass