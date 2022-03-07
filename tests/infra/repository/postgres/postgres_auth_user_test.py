import pytest
from zione.core.exceptions import MissingFieldError

from zione.domain.entities.response import Response
from zione.core.dependency_injection import make_repository

user = {"username": "kaio", "password": "kaio123"}


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_method_returns_response_instance(app):
    repo = make_repository(app)
    res = repo.auth_user(user)

    assert isinstance(res, Response)


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_all_valid_fields(app):
    repo = make_repository(app)
    res = repo.auth_user({"username": "kaio", "password": "kaio123"})

    username = res.result[0].get("username", None)
    password = res.result[0].get("password", None)

    assert username is not None
    assert password is not None


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_missing_fields(app):
    repo = make_repository(app)
    res = repo.auth_user({"username": "kaio"})

    assert res.error == MissingFieldError()


@pytest.mark.integration
@pytest.mark.db_auth_user
def test_auth_user_with_empty_password(app):
    repo = make_repository(app)
    res = repo.auth_user({"username": "kaio", "password": ""})

    assert res.error == MissingFieldError()


# @pytest.mark.integration
# @pytest.mark.db_auth_user
# def test_auth_user_table_that_dont_exist_should_return_error_on_response(app):
    repo = make_repository(app)
#     res = repo.auth_user({}, "inexistent_table")
#
#     assert res.error == DatabaseError("Error on select")
#     assert "does not exist" in res.message
