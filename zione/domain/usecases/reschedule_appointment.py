import logging

from zione.core.exceptions import InvalidValueError, MissingFieldError
from zione.core.utils.int_utils import validate_id
from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


def reschedule_appointment_usecase(repo: RepositoryInterface, entry: dict, id: int):
    """
    Reschedule an appointment.
    Receives an id and entry, and passes date, time and duration to repository update.
    """
    logging.info("[RESCHEDULE] initiating ticket close")

    try:
        record = {"id": f"{id}"}
        validate_id(id)

        logging.info("[RESCHEDULE] checking for date, time or duration to update")
        date = entry.get("date", None)
        time = entry.get("time", None)
        duration = entry.get("duration", None)

        if date is not None:
            record["date"] = date
        if time is not None:
            record["time"] = time
        if duration is not None:
            record["duration"] = duration

        if not date and not time and not duration:
            logging.info("[RESCHEDULE] no field required for reschedule found")
            raise MissingFieldError

    except MissingFieldError as e:
        logging.error(f"[RESCHEDULE] missing one or more fields: {e}")
        return Response.missing_field(e)

    except InvalidValueError as e:
        logging.error(f"[RESCHEDULE] invalid value passed to id: {id}")
        return Response.invalid_value("id")

    except Exception as e:
        logging.error(f"[RESCHEDULE] an generic error occurred: {e}")
        return Response.generic_error(e)

    else:
        logging.info("[RESCHEDULE] all requirements present, sending update request to database...")
        return repo.update(record, Appointment.endpoint)
