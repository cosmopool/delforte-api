from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.usecases.add_ticket import add_ticket_usecase

from tests.stubs.repository_stub import RepositoryStub

class TestAddTicketUsecase:
    tk_dict = {
        "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
    }

    tk = Ticket(
        id = 1,
        clientName = "Roberto Barao",
        clientAddress = "Rua David Campista, 211",
        clientPhone = 41999000888,
        serviceType = "Manutencao",
        description = "Alarme nao arma",
        isFinished = False
    )


    def test_usecase_return_response_instance(self, repo_stub):
        res = add_ticket_usecase(repo_stub, self.tk_dict)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_http_code_406(self, repo_stub):
        tk_dict = self.tk_dict
        if tk_dict.get("clientName"):
            self.tk_dict.pop("clientName")
        res = add_ticket_usecase(repo_stub, self.tk_dict)

        assert res.http_code == 406

    def test_dict_with_missings_fields_should_return_error(self, repo_stub):
        tk_dict = self.tk_dict
        if tk_dict.get("clientName"):
            self.tk_dict.pop("clientName")
        res = add_ticket_usecase(repo_stub, self.tk_dict)

        assert res.error == MissingFieldError()

    def test_dict_with_missings_fields_should_return_message(self, repo_stub):
        tk_dict = self.tk_dict
        if tk_dict.get("clientName"):
            self.tk_dict.pop("clientName")
        res = add_ticket_usecase(repo_stub, self.tk_dict)

        assert "Missing data for required field" in res.message

    def test_dict_with_missings_fields_should_return_status_error(self, repo_stub):
        tk_dict = self.tk_dict
        if tk_dict.get("clientName"):
            self.tk_dict.pop("clientName")
        res = add_ticket_usecase(repo_stub, self.tk_dict)

        assert res.status == Status.Error

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        tk_dict = self.tk.to_dict()
        if tk_dict.get("id"):
            self.tk_dict.pop("id")
        res = add_ticket_usecase(repo_stub, tk_dict)

        assert res.http_code == 200

    # def test_dict_with_missings_fields_should_return_http_code_406(self, repo_stub):
    #     pass
