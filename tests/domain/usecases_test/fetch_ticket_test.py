from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.usecases.fetch_ticket import fetch_ticket_usecase

from tests.stubs.repository_stub import RepositoryStub


class TestEditTicketUsecase:
    tk_dict = {
        "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
    }

    repository = RepositoryStub()

    def test_usecase_return_response_instance(self):
        res = fetch_ticket_usecase(self.repository, 1)

        assert isinstance(res, Response)

    def test_should_return_status_success(self):
        res = fetch_ticket_usecase(self.repository, 1)

        assert res.status == Status.Success

    def test_sould_return_open_ticket_in_result(self):
        res = fetch_ticket_usecase(self.repository, 1)

        assert res.result == [self.tk_dict.__str__()]

