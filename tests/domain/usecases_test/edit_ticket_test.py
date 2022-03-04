from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.usecases.edit_ticket import edit_ticket_usecase

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

    tk = Ticket(
        id = 1,
        clientName = "Roberto Barao",
        clientAddress = "Rua David Campista, 211",
        clientPhone = 41999000888,
        serviceType = "Manutencao",
        description = "Alarme nao arma",
        isFinished = False
    )

    repository = RepositoryStub()

    def test_usecase_return_response_instance(self):
        res = edit_ticket_usecase(self.repository, self.tk_dict)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_status_success(self):
        tk_dict = self.tk_dict
        if tk_dict.get("date"):
            self.tk_dict.pop("date")
        res = edit_ticket_usecase(self.repository, self.tk_dict)

        assert res.status == Status.Success

    def test_valid_dict_should_return_http_cod_200(self):
        tk_dict = self.tk.to_dict()
        if tk_dict.get("id"):
            self.tk_dict.pop("id")
        res = edit_ticket_usecase(self.repository, tk_dict)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self):
        tk_dict = {"id": 1, "serviceType": "Instalacao"}
        res = edit_ticket_usecase(self.repository, tk_dict)

        assert res.status == Status.Success

