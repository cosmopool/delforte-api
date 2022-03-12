from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def fetch_ticket_usecase(repo: RepositoryInterface, id: int) -> Response:
    record = {"id": f"= {id}"}
    return repo.select(record, Ticket.endpoint)
