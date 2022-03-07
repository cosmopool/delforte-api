import logging
import pytest
import random
from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError

from zione.domain.entities.response import Response

user = {"username": "kaio", "password": "minecraft"} 
logging.basicConfig(level=logging.DEBUG)


@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_method_returns_response_instance(repo):
    res = repo.insert_user({})

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_all_valid_fields(repo):
    num = random.random()
    usr = {"username": f"gusta{num}", "password": "minecraft"} 
    res = repo.insert_user(usr)
    repo.delete(2, "users")

    assert res.status == Status.Success
    assert res.error is None

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_should_return_error_trying_to_insert_same_username(repo):
    res = repo.insert_user(user)
    repo.delete(2, "users")

    assert res.status == Status.Error
    assert res.error is not None

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_missing_fields(repo):
    res = repo.insert_user({"username": "kaio"})

    assert res.error == MissingFieldError()

@pytest.mark.integration
@pytest.mark.db_insert_user
def test_insert_user_with_empty_password(repo):
    res = repo.insert_user({"username": "kaio", "password": ""})

    assert res.error == MissingFieldError()

