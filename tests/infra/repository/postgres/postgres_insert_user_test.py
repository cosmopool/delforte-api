import logging
import pytest
from zione.core.enums import Status
from zione.core.exceptions import DatabaseError, MissingFieldError

from zione.domain.entities.response import Response
from zione.infra.repositories.postgres_repository import PostgresRepository

repo = PostgresRepository()
user = {"username": "asdfas", "password": "asdfasdfaf"} 
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_method_returns_response_instance():
    res = repo.insert_user({})

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_all_valid_fields():
    username = user['username']
    res = repo.insert_user(user)
    user_id = repo.select({"username": f"= '{username}'"}, "users").result[0]['id']
    repo.delete(user_id, "users")

    assert res.status == Status.Success
    assert res.result[0] > 0

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_missing_fields():
    res = repo.insert_user({"username": "kaio"})

    assert res.error == MissingFieldError()

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_empty_password():
    res = repo.insert_user({"username": "kaio", "password": ""})

    assert res.error == MissingFieldError()

# @pytest.mark.integration
# @pytest.mark.db_insert_user
# def test_insert_user_table_that_dont_exist_should_return_error_on_response():
#     res = repo.insert_user({}, "inexistent_table")
#
#     assert res.error == DatabaseError("Error on select")
#     assert "does not exist" in res.message
