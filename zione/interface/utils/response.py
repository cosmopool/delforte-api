import logging
from zione.core.enums import Status
from zione.domain.entities.response import Response


def cook_response(raw_response: Response) -> tuple[dict, int]:
    logging.info(f"[MAKE_RESPONSE] cooking response")

    result = raw_response.result if raw_response.status == Status.Success else raw_response.message
    res = {"Status": raw_response.status.__str__(), "Result": result}, raw_response.http_code

    logging.debug(f"[MAKE_RESPONSE] ...done, response cooked: {res}")

    return res
