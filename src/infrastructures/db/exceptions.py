class MappersNoneException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'MappersNoneException: {self.message}'

class RecordsNoneException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'RecordsNoneException: {self.message}'

class RecordsNoFoundException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'RecordsNoFoundException: {self.message}'