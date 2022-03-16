from dataclasses import dataclass, asdict, field
from typing import Optional

from zione.core.enums import Status
from zione.core.exceptions import BaseError, GenericError, InvalidValueError, MissingFieldError
from zione.core.utils.dict_utils import capitalize_dict_keys


@dataclass
class Response:
    status: Status
    http_code: int
    result: list = field(default_factory=list)
    message: str = ""
    error: Optional[BaseError] = None

    @classmethod
    def missing_field(cls, err_msg: Exception):
        return cls(
            status=Status.Error,
            http_code=406,
            message=f"One or more error occured: {err_msg}",
            error=MissingFieldError(),
        )
    
    @classmethod
    def validation_error(cls, err_msg: Exception):
        return cls(
            status=Status.Error,
            http_code=406,
            message=f"One or more error occured: {err_msg}",
            error=InvalidValueError(),
        )

    @classmethod
    def authorized(cls, token: str):
        return cls(
            status=Status.Success,
            http_code=200,
            message="Login successful",
            result=[token]
        )

    @classmethod
    def not_authorized(cls, message: str):
        return cls(
            status=Status.Error,
            http_code=401,
            message=message,
        )

    @classmethod
    def invalid_value(cls, param: str):
        return cls(
            status=Status.Error,
            http_code=412,
            error=InvalidValueError(),
            message=f"One or more invalid character used in '{param}' parameter",
        )

    @classmethod
    def generic_error(cls, err: Exception):
        return cls(
            status=Status.Error,
            http_code=412,
            error=GenericError(),
            message=f"One or more error occured: {err}",
        )

    def to_dict(self):
        d = asdict(self)
        d.pop("http_code")

        return capitalize_dict_keys(d), self.http_code
