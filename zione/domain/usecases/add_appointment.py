import logging

from marshmallow.utils import EXCLUDE
from marshmallow.exceptions import ValidationError

from zione.domain.entities.response import Response
from zione.infra.schemas.appointments import AppointmentSchema
from zione.domain.entities.appointment import Appointment
from zione.domain.repository_interface import RepositoryInterface


def add_appointment_usecase(repo: RepositoryInterface, entry: dict) -> Response:
    """
    Add an appointment.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """
    logging.info("[ADD][APPOINTMENT] initiating appointment insertion")

    try:
        schema = AppointmentSchema(partial=False).load(entry, unknown=EXCLUDE)
        logging.debug(f"[ADD][APPOINTMENT] schema loaded: {schema}")
        record = Appointment.from_dict(schema)
        logging.debug(f"[ADD][APPOINTMENT] ticket: {record}")

    except ValidationError as e:
        logging.error(f"[ADD][TICKET] error validating data: {e}")
        return Response.missing_field(e)

    except Exception as e:
        logging.error(f"[ADD][APPOINTMENT] error validating data {e}")
        return Response.missing_field(e)

    else:
        logging.info("[ADD][APPOINTMENT] all requirements present, sending insert request to database database...")
        return repo.insert(record.to_dict(), Appointment.endpoint)
