import pytest

from zione.domain.entities.response import Response


@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_method_returns_response_instance(repo, tk):
    res = repo.insert(tk, "tickets")

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_valid_ticket(repo, tk):
    res = repo.insert(tk, "tickets")

    assert res.result[0] > 0

@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_valid_appointment(repo, ap):
    res = repo.insert(ap, "appointments")

    assert res.result[0] > 0
