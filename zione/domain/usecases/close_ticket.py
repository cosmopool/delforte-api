import logging

from zione.core.exceptions import InvalidValueError
from zione.core.utils.int_utils import validate_id
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def close_ticket_usecase(repo: RepositoryInterface, id: int):
    """
    Closes an ticket.
    Receives an id and then sends a query to repository.
    """
    logging.info("[CLOSE][APPOINTMENT] initiating ticket close")

    try:
        validate_id(id)

    except InvalidValueError as e:
        logging.error(f"[CLOSE][APPOINTMENT] invalid value passed to id: {id}")
        return Response.invalid_value("id")

    except Exception as e:
        logging.error(f"[CLOSE][APPOINTMENT] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[CLOSE][APPOINTMENT] all requirements present, sending update request to database...")
        return repo.update({"id": f"{id}", "isFinished": "true"}, Ticket.endpoint)
