from dataclasses import dataclass

from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


@dataclass
class RepositoryStub(RepositoryInterface):
    """Appointments repository"""

    table: str = "appointments"

    def insert(self, entry: dict[str, str], table: str) -> Response:
        """Add an entry to the database"""
        return Response(status=Status.Success, result=[1], http_code=200)

    def delete(self, id: int, table: str) -> Response:
        """Remove an entry from the database"""
        return Response(status=Status.Success, result=[1], http_code=200)

    def update(self, entry: dict[str, str], table: str, id: int = -1) -> Response:
        """Edit an entry in the database"""
        return Response(status=Status.Success, result=[1], http_code=200)

    def select(self, entry: dict[str, str], table: str) -> Response:
        """Fetch an entry from the database"""
        is_open = entry == {"isFinished": "= false"}
        entry_id = entry.get("id") == "= 1"
        tk_dict = {
            "id": 1,
            "clientName": "Roberto Barao",
            "clientAddress": "Rua David Campista, 211",
            "clientPhone": 41999000888,
            "serviceType": "Manutencao",
            "description": "Alarme nao arma",
            "isFinished": False
        }
        ap_dict = {
            "id": 1,
            "time": "10:00",
            "date": "12-12-2021",
            "duration": "1:00",
            "ticketId": 1,
            "isFinished": False,
        }
        agenda_dict = {
            "id": 1,
            "time": "10:00",
            "date": "12-12-2021",
            "duration": "1:00",
            "ticketId": 1,
            "clientName": "Roberto Barao",
            "clientAddress": "Rua David Campista, 211",
            "clientPhone": 41999000888,
            "serviceType": "Manutencao",
            "description": "Alarme nao arma",
            "isFinished": False,
        }
        usr_dict = {
            "id": 2,
            "username": "lucca",
            "password": "cocomelon"
        }

        if entry_id and table == "tickets":
            return Response(status=Status.Success, result=[tk_dict.__str__()], http_code=200)
        if entry_id and table == "appointments":
            return Response(status=Status.Success, result=[ap_dict.__str__()], http_code=200)
        if entry_id and table == "users":
            return Response(status=Status.Success, result=[usr_dict.__str__()], http_code=200)

        if is_open and table == "tickets":
            return Response(status=Status.Success, result=[tk_dict.__str__()], http_code=200)
        if is_open and table == "appointments":
            return Response(status=Status.Success, result=[ap_dict.__str__()], http_code=200)
        if is_open and table == "agenda":
            return Response(status=Status.Success, result=[agenda_dict.__str__()], http_code=200)
        else:
            return Response(status=Status.Success, result=[1], http_code=200)

    def insert_user(self, entry: dict[str, str]) -> Response:
        """Fetch an entry from the database"""
        return Response(status=Status.Success, result=[1], http_code=200)

    def auth_user(self, entry: dict[str, str]) -> Response:
        """Fetch an entry from the database"""
        return Response(status=Status.Success, result=[1], http_code=200)
