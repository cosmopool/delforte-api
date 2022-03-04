import pytest

from zione.core.exceptions import DatabaseError
from zione.domain.entities.response import Response
from zione.infra.repositories.postgres_repository import PostgresRepository


repo = PostgresRepository()
ap = {
    "time": "10:00",
    "date": "12-12-2021",
    "duration": "1:00",
    "ticketId": 43,
    "isFinished": False,
}
tk = {
    # "id": 55,
    "clientName": "Roberto Barao",
    "clientAddress": "Rua David Campista, 211",
    "clientPhone": 41999000888,
    "serviceType": "Manutencao",
    "description": "Alarme nao arma",
    "isFinished": False,
}


@pytest.mark.integration
@pytest.mark.db_delete
def test_delete_returns_response_instance():
    res = repo.delete(0, "appointments")

    assert isinstance(res, Response)


@pytest.mark.integration
@pytest.mark.db_delete
@pytest.mark.slow
def test_delete_appointment_by_id():
    insert_res = repo.insert(ap, "appointments")
    ap_id = insert_res.result[0]
    res = repo.delete(ap_id, "appointments")

    assert res.result == [1]
    assert ap_id > 0


@pytest.mark.integration
@pytest.mark.db_delete
@pytest.mark.slow
def test_delete_ticket_by_id():
    insert_res = repo.insert(tk, "tickets")
    tk_id = insert_res.result[0]
    res = repo.delete(tk_id, "tickets")

    assert res.result == [1]
    assert tk_id > 0


@pytest.mark.integration
@pytest.mark.db_delete
def test_delete_entry_on_table_that_dont_exist_should_return_error_on_response():
    res = repo.delete(0, "inexistent_table")

    assert res.error == DatabaseError("Error on delete")
