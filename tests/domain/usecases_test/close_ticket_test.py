from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.entities.ticket import Ticket
from zione.domain.usecases.close_ticket import close_ticket_usecase

from tests.stubs.repository_stub import RepositoryStub


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

    repository = RepositoryStub()

    def test_usecase_return_response_instance(self):
        res = close_ticket_usecase(self.repository, self.tk.id)

        assert isinstance(res, Response)

    def test_invalid_id_number(self):
        res = close_ticket_usecase(self.repository, -4)

        assert res.status == Status.Error
        assert res.http_code == 406

    def test_string_instead_of_int(self):
        res = close_ticket_usecase(self.repository, "1")

        assert res.error == InvalidValueError()
        assert "Invalid field value" in res.message

    def test_None_instead_of_int(self):
        res = close_ticket_usecase(self.repository, None)

        assert res.status == Status.Error
        assert "Invalid field value" in res.message

    def test_valid_dict_should_return_http_cod_200(self):
        res = close_ticket_usecase(self.repository, self.tk.id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self):
        res = close_ticket_usecase(self.repository, self.tk.id)

        assert res.status == Status.Success

