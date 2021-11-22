from enum import Enum, auto

class QueryType(Enum):
    UPDATE = auto()
    SELECT = auto()
    INSERT = auto()
    DELETE = auto()
    INSERT_USER = auto()
    AUTH_USER = auto()

