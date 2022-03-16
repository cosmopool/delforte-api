from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.usecases.close_ticket import close_ticket_usecase



class TestCloseTicketUsecase:
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
        res = close_ticket_usecase(repo_stub, self.tk.id)

        assert isinstance(res, Response)

    def test_invalid_id_number(self, repo_stub):
        res = close_ticket_usecase(repo_stub, -4)

        assert res.status == Status.Error
        assert res.http_code == 412

    def test_invalid_string(self, repo_stub):
        res = close_ticket_usecase(repo_stub, "a")
        print(res)

        assert res.status == Status.Error
        assert "invalid character" in res.message.lower()

    def test_string_instead_of_int(self, repo_stub):
        res = close_ticket_usecase(repo_stub, "1")

        assert res.status == Status.Success

    def test_None_instead_of_int(self, repo_stub):
        res = close_ticket_usecase(repo_stub, None)

        assert res.status == Status.Error
        assert "not" in res.message.lower()
        assert "nonetype" in res.message.lower()

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        res = close_ticket_usecase(repo_stub, self.tk.id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub):
        res = close_ticket_usecase(repo_stub, self.tk.id)

        assert res.status == Status.Success

