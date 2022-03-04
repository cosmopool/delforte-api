import logging
from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.user import User
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.users import UserSchema


def authenticate_user_usecase(repo: RepositoryInterface, user: dict, create_token_callback) -> Response:
    """Athenticate a user credentials and return access token if everything matches"""

    try:
        schema = UserSchema(partial=False).load(user)
        record = User.from_dict(schema)
    except Exception as e:
        logging.error(e)
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=f"Missing data for required field {e.__str__()}",
        )
    else:
        authentication = repo.select(record.to_dict(), "users")
        if authentication.status == Status.Success:
            token = create_token_callback(identity=record.username)
            return Response(
                status=Status.Success,
                http_code=200,
                message="Login successful",
                result=[token]
            )
        else:
            message = "Couldn't login. Confirm your credentials."
            return Response(
                status=Status.Success,
                http_code=200,
                message=message,
                result=[message],
            )
