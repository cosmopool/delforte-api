from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.core.utils.int_utils import validate_id
from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


def reschedule_appointment_usecase(repo: RepositoryInterface, entry: dict, id: int):
    """
    Reschedule an appointment.
    Receives an id and entry, and passes date, time and duration to repository update.
    """
    record = {"id": f"{id}"}
    id_is_valid = validate_id(id)
    date = entry.get("date", None)
    time = entry.get("time", None)
    duration = entry.get("duration", None)

    if date is not None:
        record["date"] = date
    if time is not None:
        record["time"] = time
    if duration is not None:
        record["duration"] = duration

    if id_is_valid and (date or time or duration):
        return repo.update(record, Appointment.endpoint)
    else:
        return Response(
            status=Status.Error,
            http_code=406,
            message="Invalid field value: 'id'",
            error=InvalidValueError(),
        )
