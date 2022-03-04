import pytest
from zione.core.exceptions import DatabaseError, MissingFieldError

from zione.domain.entities.response import Response
from zione.infra.repositories.postgres_repository import PostgresRepository

repo = PostgresRepository()
user = {"username": "kaio", "password": "kaio123"}


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_method_returns_response_instance():
    res = repo.auth_user(user)

    assert isinstance(res, Response)


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_all_valid_fields():
    res = repo.auth_user({"username": "kaio", "password": "kaio123"})

    assert res.result[0] == {
        "id": 3,
        "password": "$2a$06$xkUaWviKJtbDdO5mbY.fqebyMScPXJMRxkrcceoz1VS.FvK0sW3tW",
        "username": "kaio",
    }


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_missing_fields():
    res = repo.auth_user({"username": "kaio"})

    assert res.error == MissingFieldError()


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_empty_password():
    res = repo.auth_user({"username": "kaio", "password": ""})

    assert res.error == MissingFieldError()


# @pytest.mark.integration
# @pytest.mark.db_auth_user
# def test_auth_user_table_that_dont_exist_should_return_error_on_response():
#     res = repo.auth_user({}, "inexistent_table")
#
#     assert res.error == DatabaseError("Error on select")
#     assert "does not exist" in res.message
