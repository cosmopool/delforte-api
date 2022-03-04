from zione.core.enums import Status
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
    id_is_valid = validate_id(id)

    if id_is_valid:
        return repo.update({"id": f"{id}", "isFinished": "true"}, Ticket.endpoint)
    else:
        return Response(
            status=Status.Error,
            http_code=406,
            message="Invalid field value: 'id'",
            error=InvalidValueError(),
        )
