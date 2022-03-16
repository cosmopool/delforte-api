import logging

from marshmallow.exceptions import ValidationError

from zione.core.exceptions import InvalidValueError, MissingFieldError
from zione.core.utils.int_utils import validate_id
from zione.core.utils.string_utils import validate_param_values
from zione.domain.entities.response import Response
from zione.domain.entities.appointment import Appointment
from zione.domain.repository_interface import RepositoryInterface


def fetch_appointment_usecase(repo: RepositoryInterface, id: int) -> Response:
    """Return a ticket data by it's id"""
    logging.info("[FETCH][APPOINTMENT] starting fetching ticket by id")

    try:
        validate_id(id)
        logging.debug(f"[FETCH][APPOINTMENT] id value: {id}")
        validate_param_values(id.__str__())

    except InvalidValueError as e:
        logging.error(f"[FETCH][APPOINTMENT] invalid character passed to id: {e}")
        return Response.invalid_value("id")

    except MissingFieldError as e:
        logging.error(f"[FETCH][APPOINTMENT] missing field: {e}")
        return Response.missing_field(e)

    except ValidationError as e:
        logging.error(f"[FETCH][APPOINTMENT] missing field: {e}")
        return Response.missing_field(e)

    except Exception as e:
        logging.error(f"[FETCH][APPOINTMENT] generic error: {e}")
        return Response.validation_error(e)

    else:
        record = {"id": f"= {id}"}
        return repo.select(record, Appointment.endpoint)
