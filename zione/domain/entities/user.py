from dataclasses import dataclass

from zione.domain.entities.entity import Entity


@dataclass
class User(Entity):
    username: str
    password: str
    id: int = -1
    endpoint = "users"
