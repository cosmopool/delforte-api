import logging
from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.usecases.edit_ticket import edit_ticket_usecase


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

    def test_usecase_return_response_instance(self, repo_stub):
        id = self.tk_dict['id']
        res = edit_ticket_usecase(repo_stub, self.tk_dict, id)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_status_success(self, repo_stub):
        tk_dict = self.tk_dict
        id = self.tk_dict['id']
        if tk_dict.get("date"):
            self.tk_dict.pop("date")
        res = edit_ticket_usecase(repo_stub, self.tk_dict, id)

        assert res.status == Status.Success

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        tk_dict = self.tk.to_dict()
        id = self.tk_dict['id']
        if tk_dict.get("id"):
            self.tk_dict.pop("id")
        res = edit_ticket_usecase(repo_stub, tk_dict, id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub, caplog):
        caplog.set_level(logging.DEBUG)
        tk_dict = {"id": 1, "serviceType": "Instalacao"}
        id = tk_dict['id']
        res = edit_ticket_usecase(repo_stub, tk_dict, id)

        assert res.status == Status.Success

