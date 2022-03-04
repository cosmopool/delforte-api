from dataclasses import dataclass, asdict, field
from typing import Optional

from zione.core.enums import Status
from zione.core.exceptions import BaseError
from zione.core.utils.dict_utils import capitalize_dict_keys

@dataclass
class Response:
    status: Status
    http_code: int
    result: list = field(default_factory=list)
    message: str = ""
    error: Optional[BaseError] = None

    def to_dict(self):
        d = asdict(self)
        d.pop('http_code')

        return capitalize_dict_keys(d), self.http_code
