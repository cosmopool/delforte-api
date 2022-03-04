from zione.core.enums import Status
from zione.core.utils.int_utils import validate_id
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.repository_interface import RepositoryInterface


def delete_ticket_usecase(repo: RepositoryInterface, id: int):
    """Delete an ticket"""

    id_is_valid = validate_id(id)

    if id_is_valid:
        return repo.delete(id, Ticket.endpoint)
    else:
        return Response(status=Status.Error, http_code=406, message="Invalid field value: 'id'", error=InvalidValueError())
