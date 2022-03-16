import logging

from zione.core.exceptions import InvalidValueError
from zione.core.utils.int_utils import validate_id
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def edit_ticket_usecase(repo: RepositoryInterface, entry: dict, id: int) -> Response:
    """
    Edit an ticket.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """
    logging.info("[EDIT][TICKET] initiating ticket edit")

    try:
        validate_id(id)

        logging.info(f"[EDIT][TICKETS] setting entry id: {id}")
        entry['id'] = int(id)

    except InvalidValueError as e:
        logging.error(f"[EDIT][TICKET] an generic error occurred: {e}")
        return Response.invalid_value("id")

    except Exception as e:
        logging.error(f"[EDIT][TICKET] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[EDIT][TICKET] all requirements present, sending update request to database...")
        return repo.update(entry, Ticket.endpoint)
