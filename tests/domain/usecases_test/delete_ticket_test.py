from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.usecases.delete_ticket import delete_ticket_usecase

from tests.stubs.repository_stub import RepositoryStub

class TestDeleteTicketUsecase:
    repository = RepositoryStub()

    def test_return_response_instance(self):
        res = delete_ticket_usecase(self.repository, 1)

        assert isinstance(res, Response)

    def test_valid_id_number(self):
        res = delete_ticket_usecase(self.repository, 1)

        assert isinstance(res, Response)

    def test_invalid_id_number(self):
        res = delete_ticket_usecase(self.repository, -4)

        assert res.status == Status.Error
        assert res.http_code == 406

    def test_string_instead_of_int(self):
        res = delete_ticket_usecase(self.repository, "1")

        assert res.error == InvalidValueError()
        assert "Invalid field value" in res.message

    def test_None_instead_of_int(self):
        res = delete_ticket_usecase(self.repository, None)

        assert res.status == Status.Error
        assert "Invalid field value" in res.message

