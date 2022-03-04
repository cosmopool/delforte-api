import logging
from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.user import User
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.schemas.users import UserSchema


def add_user_usecase(repo: RepositoryInterface, entry: dict):
    """
    Add an user.
    Receives an entry, validates it's fields by deserializing and then passes to the repository.
    """

    try:
        schema = UserSchema(partial=False).load(entry)
        record = User.from_dict(schema)
    except Exception as e:
        logging.error(e)
        return Response(
            status=Status.Error,
            http_code=406,
            error=MissingFieldError(),
            message=e.__str__(),
        )
    else:
        return repo.insert_user(record.to_dict())
