import pytest

from zione.domain.entities.response import Response
from zione.infra.repositories.postgres_repository import PostgresRepository

repo = PostgresRepository()
ap = {"time": "10:00", "date": "12-12-2021", "duration": "1:00", "ticketId": 43, "isFinished": False}
tk = {
    # "id": 1,
    "clientName": "Roberto Barao",
    "clientAddress": "Rua David Campista, 211",
    "clientPhone": 41999000888,
    "serviceType": "Manutencao",
    "description": "Alarme nao arma",
    "isFinished": False
}

@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_method_returns_response_instance():
    res = repo.insert(tk, "tickets")

    assert isinstance(res, Response)

@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_valid_ticket():
    res = repo.insert(tk, "tickets")

    assert res.result[0] > 0

@pytest.mark.integration
@pytest.mark.db_insert
def test_insert_valid_appointment():
    res = repo.insert(ap, "appointments")

    assert res.result[0] > 0
