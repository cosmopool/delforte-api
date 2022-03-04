import logging
from dataclasses import dataclass

@dataclass
class BaseError(Exception):
    class_msg: str = ""

    def __init__(self, msg: str = "Generic error"):
        self.msg = msg
        logging.error(msg, exc_info=self)

    def __str__(self):
        return f"{self.class_msg} || {self.msg}"

    def __eq__(self, other):
        return self.__str__() == other.__str__()


class DatabaseError(BaseError):
    """Database error"""
    class_msg = "Database error"

class MissingFieldError(BaseError):
    """Missing fields error"""
    class_msg = "There's one or more missings required fields"

class InvalidValueError(BaseError):
    """When the value received is invalid"""
    class_msg = "There's one or more field with invalid value"
