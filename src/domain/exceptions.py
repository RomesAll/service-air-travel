from typing import final

@final
class DomainValidationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f'DomainValidationError: {self.message}'

@final
class InvalidTownError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f'InvalidTownError: {self.message}'