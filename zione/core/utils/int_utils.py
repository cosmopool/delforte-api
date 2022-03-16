import logging
from typing import Any

from zione.core.exceptions import InvalidValueError, MissingFieldError


def validate_id(id: Any) -> bool:
    """Return true if given id is a valid integer for quering entries in database"""
    logging.info("[INT][VALIDATION] testing integer for range and value")

    try:
        logging.info("[INT][VALIDATION] attempting to cast given argument to integer")
        _id = int(id)

    except ValueError:
        logging.error(f"[INT][VALIDATION] given parameter is not an integer: {id}")
        raise InvalidValueError

    except Exception as e:
        logging.error(f"[INT][VALIDATION] could not cast to integer: {e}")
        raise e

    else:
        is_string = isinstance(_id, str)
        is_negative_or_zero = isinstance(_id, int) and _id <= 0

        if _id is None:
            logging.error("[INT][VALIDATION] given parameter is empty")
            raise MissingFieldError

        if is_negative_or_zero or is_string:
            logging.error("[INT][VALIDATION] given integer has invalid value or range")
            raise InvalidValueError
            
        else:
            logging.info("[INT][VALIDATION] given integer is valid!")
            return True
