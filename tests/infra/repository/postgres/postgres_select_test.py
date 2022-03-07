import pytest
from zione.core.exceptions import DatabaseError

from zione.domain.entities.response import Response


@pytest.mark.integration
@pytest.mark.db_select
def test_select_method_returns_response_instance(repo):
    res = repo.select({"id": "= 2"}, "appointments")

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_select
def test_select_appointment_by_id(repo):
    res = repo.select({"id": "= 1"}, "appointments")

    assert res.result[0]['id'] == 1
    assert res.result[0]['ticketId'] == 1

@pytest.mark.integration
@pytest.mark.db_select
def test_select_ticket_by_id(repo):
    res = repo.select({"id": "= 1"}, "tickets")

    assert res.result[0]['id'] == 1

@pytest.mark.integration
@pytest.mark.db_select
def test_select_all_agenda_entries(repo):
    res = repo.select({"isFinished": "= false"}, "agenda")

    assert len(res.result) > 0

@pytest.mark.integration
@pytest.mark.db_select
def test_select_all_appointments(repo):
    res = repo.select({}, "appointments")

    assert len(res.result) > 0

@pytest.mark.integration
@pytest.mark.db_select
def test_select_table_that_dont_exist_should_return_error_on_response(repo):
    res = repo.select({}, "inexistent_table")

    assert res.error == DatabaseError("Error on select")
    assert "does not exist" in res.message

# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets(repo):
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets(repo):
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets(repo):
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
