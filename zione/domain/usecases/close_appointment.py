from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.core.utils.int_utils import validate_id
from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


def close_appointment_usecase(repo: RepositoryInterface, id: int):
    """
    Closes an appointment.
    Receives an id and then sends a query to repository.
    """
    id_is_valid = validate_id(id)

    if id_is_valid:
        return repo.update({"id": f"{id}", "isFinished": "true"}, Appointment.endpoint)
    else:
        return Response(
            status=Status.Error,
            http_code=406,
            message="Invalid field value: 'id'",
            error=InvalidValueError(),
        )
