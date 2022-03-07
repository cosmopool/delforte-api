import pytest
from zione.core.exceptions import DatabaseError

from zione.domain.entities.response import Response

ap_ref = {
    "time": "10:00",
    "date": "12-12-2021",
    "duration": "1:00",
    "ticketId": 1,
    "isFinished": False,
}
tk_ref = {
    "clientName": "Roberto Barao",
    "clientAddress": "Rua David Campista, 211",
    "clientPhone": 41999000888,
    "serviceType": "Manutencao",
    "description": "Alarme nao arma",
    "isFinished": False,
}


@pytest.mark.integration
@pytest.mark.db_update
def test_update_returns_response_instance(repo):
    res = repo.update({}, "appointments", 7)

    assert isinstance(res, Response)


@pytest.mark.integration
@pytest.mark.db_update
@pytest.mark.slow
def test_update_appointment_by_id(repo):
    ap = {
        "id": 1,
        "date": "2021-12-12",
        "time": "10:00:00",
        "duration": "01:00:00",
        "ticketId": 1,
        "isFinished": False,
    }
    res = repo.update(ap, "appointments", ap["id"])

    assert res.result == [1]


@pytest.mark.integration
@pytest.mark.db_update
@pytest.mark.slow
def test_update_ticket_by_id(repo):
    tk = {
        "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41888000999,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False,
    }
    res = repo.update(tk, "tickets", tk["id"])

    assert res.result == [1]


@pytest.mark.integration
@pytest.mark.db_update
def test_update_table_that_dont_exist_should_return_error_on_response(repo):
    res = repo.update(ap_ref, "inexistent_table", 1)

    assert res.error == DatabaseError("Error on update")


@pytest.mark.integration
@pytest.mark.db_update
def test_update_entry_without_passing_id_separated(repo):
    tk = {
        "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41888000777,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False,
    }
    res = repo.update(tk, "tickets")

    assert res.result == [1]
