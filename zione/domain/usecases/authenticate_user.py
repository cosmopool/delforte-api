import logging

from marshmallow.exceptions import ValidationError

from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError, MissingFieldError
from zione.core.utils.string_utils import validate_param_values
from zione.domain.entities.response import Response
from zione.domain.entities.user import User
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.users import UserSchema


def authenticate_user_usecase(repo: RepositoryInterface, user: dict, create_token_callback) -> Response:
    """Athenticate a user credentials and return access token if everything matches"""
    logging.info("[AUTH] starting athentication")

    # if username is not None and has_sql_injection(username):
    #     return Response.invalid_value("username")

    try:
        logging.info("[AUTH] validating fields")
        schema = UserSchema(partial=False).load(user)
        logging.debug(f"[AUTH] schema loaded: {schema}")
        record = User.from_dict(schema)
        logging.debug(f"[AUTH] user: {record}")

        username = user.get("username")
        validate_param_values(username)

    except InvalidValueError as e:
        logging.error(f"[AUTH] invalid character passed to username: {user.get('username')}")
        return Response.invalid_value("username")

    except MissingFieldError as e:
        logging.error(f"[AUTH] missing field: {e}")
        return Response.missing_field(e)

    except ValidationError as e:
        logging.error(f"[AUTH] missing field: {e}")
        return Response.missing_field(e)

    except Exception as e:
        logging.error(f"[AUTH] error authenticating: {e}")
        return Response.validation_error(e)

    else:
        logging.info("[AUTH] all requirements present, authenticating credentials with database...")

        authentication = repo.auth_user(record.to_dict())
        if authentication.status == Status.Success:
            logging.info("[AUTH] authenticated! sending token back to user")
            token = create_token_callback(identity=record.username)
            logging.debug(f"[AUTH] token: {token}")

            return Response.authorized(token)

        else:
            logging.info("[AUTH] not authenticated! sending response back to user")
            message = "Couldn't login. Confirm your credentials."
            return Response.not_authorized(message)
