import logging
from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.tickets import TicketSchema


def add_ticket_usecase(repo: RepositoryInterface, entry: dict):
    """
    Add an ticket.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """

    try:
        schema = TicketSchema(partial=False).load(entry)
        record = Ticket.from_dict(schema)
    except Exception as e:
        logging.error(e)
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=e.__str__(),
        )
    else:
        return repo.insert(record.to_dict(), Ticket.endpoint)
