import logging

from zione.core.utils.int_utils import validate_id
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def delete_ticket_usecase(repo: RepositoryInterface, id: int):
    """
    Delete an ticket.
    Receives and validate an id and then sends a query to repository.
    """
    logging.info("[DELETE][TICKET] initiating ticket close")

    try:
        validate_id(id)

    except InvalidValueError as e:
        logging.error(f"[DELETE][TICKET] invalid value passed to id: {id}")
        return Response.invalid_value("id")

    except Exception as e:
        logging.error(f"[DELETE][TICKET] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[DELETE][TICKET] all requirements present, sending delete request to database...")
        return repo.delete(id, Ticket.endpoint)
