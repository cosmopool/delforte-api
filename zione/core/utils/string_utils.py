import json
import logging

from marshmallow.exceptions import ValidationError

from zione.core.exceptions import InvalidValueError, MissingFieldError


def to_camel_case(text: str, separator: str) -> str:
    tmp = text.split(separator)
    if len(text) == 0:
        return text
    return tmp[0] + "".join(i.capitalize() for i in tmp[1:])


def validation_err_to_string(error: ValidationError) -> str:
    res = ""
    err = json.loads(error.__str__())
    for key, val in err:
        res += f"{key}: {val};"

    return res


def validate_param_values(string: str) -> bool:
    """Check if string has any invalid characters commonly used in sql injection"""
    logging.info("[STRING][VALIDATION] testing string for invalid characters used in sql injection")

    has_double_quote = '"' in string
    has_single_quote = "'" in string
    has_dash = "-" in string
    has_equal = "=" in string
    has_semi_colon = ";" in string

    if string is None:
        raise MissingFieldError

    if has_double_quote or has_single_quote or has_dash or has_equal or has_semi_colon:
        logging.error("[STRING][VALIDATION] given string has invalid characters")
        raise InvalidValueError

    else:
        logging.info("[STRING][VALIDATION] given string is valid!")
        return False
