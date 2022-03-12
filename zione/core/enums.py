from enum import Enum


class BaseEnum(Enum):
    """Base enum that return just enum name when used __str__()"""

    def __str__(self):
        return self.name


class Status(BaseEnum):
    """Enum for response status"""

    Success = "Success"
    Error = "Error"
