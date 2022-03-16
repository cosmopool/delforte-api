import logging

from marshmallow.utils import EXCLUDE
from marshmallow.exceptions import ValidationError

from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.tickets import TicketSchema


def add_ticket_usecase(repo: RepositoryInterface, entry: dict) -> Response:
    """
    Add an ticket.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """
    logging.info("[ADD][TICKET] initiating ticket insertion")

    try:
        schema = TicketSchema(partial=False).load(entry, unknown=EXCLUDE)
        logging.debug(f"[ADD][TICKET] schema loaded: {schema}")
        record = Ticket.from_dict(schema)
        logging.debug(f"[ADD][TICKET] ticket: {record}")

    except ValidationError as e:
        logging.error(f"[ADD][TICKET] error validating data: {e}")
        return Response.missing_field(e)

    except Exception as e:
        logging.error(f"[ADD][TICKET] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[ADD][TICKET] all requirements present, sending insert request to database...")
        return repo.insert(record.to_dict(), Ticket.endpoint)
