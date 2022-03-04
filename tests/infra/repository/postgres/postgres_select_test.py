import pytest
from zione.core.exceptions import DatabaseError

from zione.domain.entities.response import Response
from zione.infra.repositories.postgres_repository import PostgresRepository

repo = PostgresRepository()

@pytest.mark.integration
@pytest.mark.db_select
def test_select_method_returns_response_instance():
    res = repo.select({"id": "= 7"}, "appointments")

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_select
def test_select_appointment_by_id():
    res = repo.select({"id": "= 7"}, "appointments")

    assert res.result[0]['id'] == 7
    assert res.result[0]['ticketId'] == 43

@pytest.mark.integration
@pytest.mark.db_select
def test_select_ticket_by_id():
    res = repo.select({"id": "= 43"}, "tickets")

    assert res.result[0]['id'] == 43

@pytest.mark.integration
@pytest.mark.db_select
def test_select_all_agenda_entries():
    res = repo.select({"isFinished": "= false"}, "entry")

    assert len(res.result) > 0

@pytest.mark.integration
@pytest.mark.db_select
def test_select_all_appointments():
    res = repo.select({}, "appointments")

    assert len(res.result) > 0

@pytest.mark.integration
@pytest.mark.db_select
def test_select_table_that_dont_exist_should_return_error_on_response():
    res = repo.select({}, "inexistent_table")

    assert res.error == DatabaseError("Error on select")
    assert "does not exist" in res.message

# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets():
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets():
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
# @pytest.mark.integration
# @pytest.mark.db_select
# def test_select_all_tickets():
#     res = repo.select({}, "tickets")
#
#     assert len(res.result) > 0
#
