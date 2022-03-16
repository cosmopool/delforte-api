import logging

from zione.core.utils.int_utils import validate_id
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


def delete_appointment_usecase(repo: RepositoryInterface, id: int):
    """Delete an appointment"""
    logging.info("[DELETE][APPOINTMENT] initiating ticket close")

    try:
        validate_id(id)

    except InvalidValueError as e:
        logging.error(f"[DELETE][APPOINTMENT] invalid value passed to id: {id}")
        return Response.invalid_value("id")

    except Exception as e:
        logging.error(f"[DELETE][APPOINTMENT] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[DELETE][APPOINTMENT] all requirements present, sending delete request to database...")
        return repo.delete(id, Appointment.endpoint)
