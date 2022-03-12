from dataclasses import dataclass

from zione.domain.entities.entity import Entity


@dataclass
class Ticket(Entity):
    clientName: str
    clientAddress: str
    clientPhone: int
    serviceType: str
    description: str
    isFinished: bool
    id: int = -1
    endpoint = "tickets"
