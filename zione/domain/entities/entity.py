from abc import ABC
import logging
from typing import TypeVar
from dataclasses import dataclass, asdict

from zione.core.exceptions import MissingFieldError

T = TypeVar("T", str, int)


@dataclass
class Entity(ABC):
    @classmethod
    def from_dict(cls, d):
        """
        Return a instance given a dictionary, ignoring additional fields
        only using the ones necessary to this class. Raise exception if there is
        any missing fields.
        """
        logging.info("[ENTITY] starting deserialization from dictionary")

        tmp = {}
        for prop in cls.__dataclass_fields__:
            val = d.get(prop, None)
            if val is not None:
                tmp[prop] = val

        try:
            instance = cls(**tmp)
        except KeyError:
            raise MissingFieldError("Missing field")
        except Exception as err:
            logging.error(f"[ENTITY] Error while deserializing JSON {err}")
            raise err
        else:
            return instance

    def to_dict(self) -> dict[str, T]:
        """Return object as dictionary"""
        d = asdict(self)
        if self.id and self.id <= 0:
            d.pop("id")

        return d
