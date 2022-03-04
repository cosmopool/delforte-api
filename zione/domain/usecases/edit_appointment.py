from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.appointments import AppointmentSchema


def edit_appointment_usecase(repo: RepositoryInterface, entry: dict):
    """
    Add an appointment.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """

    try:
        record = AppointmentSchema(partial=True).load(entry)
    except Exception as e:
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=e.__str__(),
        )
    else:
        return repo.update(record, Appointment.endpoint)
