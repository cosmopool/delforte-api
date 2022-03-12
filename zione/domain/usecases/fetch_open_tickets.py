from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def fetch_open_tickets_usecase(repo: RepositoryInterface):
    return repo.select({"isFinished": "= false"}, Ticket.endpoint)
