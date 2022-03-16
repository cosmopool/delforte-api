from dataclasses import dataclass

from zione.domain.entities.entity import Entity


@dataclass
class Appointment(Entity):
    time: str
    date: str
    duration: str
    ticketId: int
    isFinished: bool = False
    id: int = -1
    endpoint = "appointments"
