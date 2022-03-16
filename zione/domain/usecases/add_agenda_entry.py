import logging

from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_appointment import add_appointment_usecase
from zione.domain.usecases.add_ticket import add_ticket_usecase


def add_agenda_entry_usecase(repo: RepositoryInterface, entry: dict) -> Response:
    """
    Add an ticket.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """

    logging.info("[ADD][AGENDA] initiating agenda entry insertion")
    ap_response = None
    tk_response = add_ticket_usecase(repo, entry)
    if tk_response.status is Status.Success:
        logging.info("[ADD][AGENDA] ticket added with success. Inserting ticketId on entry to try add appointment")
        entry["ticketId"] = tk_response.result[0]
        ap_response = add_appointment_usecase(repo, entry)
    else:
        logging.info("[ADD][AGENDA] could not add ticket. Sending error response back to user and aborting appointment insertion")
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=f"Error saving ticket. None of the entries was inserted. {tk_response.message}",
        )

    if ap_response is not None and ap_response.status is Status.Success:
        logging.info("[ADD][AGENDA] ticket added with success. Sending successful response back to user")
        return ap_response
    else:
        logging.info("[ADD][AGENDA] could not add appointment. Sending error response back to user")
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=f"Error saving appointment. {ap_response.message}. Only ticket was inserted, with id: {tk_response.result[0]}.",
        )
