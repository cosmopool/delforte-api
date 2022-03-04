from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.infra.schemas.appointments import AppointmentSchema
from zione.domain.entities.appointment import Appointment
from zione.domain.repository_interface import RepositoryInterface


def add_appointment_usecase(repo: RepositoryInterface, entry: dict):
    """
    Add an appointment.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """

    try:
        schema = AppointmentSchema(partial=False).load(entry)
        record = Appointment.from_dict(schema)
    except Exception as e:
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=e.__str__(),
        )
    else:
        return repo.insert(record.to_dict(), Appointment.endpoint)
