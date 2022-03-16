from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.usecases.delete_ticket import delete_ticket_usecase


class TestDeleteTicketUsecase:

    def test_return_response_instance(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, 1)

        assert isinstance(res, Response)

    def test_valid_id_number(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, 1)

        assert isinstance(res, Response)

    def test_invalid_id_number(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, -4)

        assert res.status == Status.Error
        assert res.http_code == 412

    def test_invalid_string(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, "a")

        assert res.status == Status.Error
        assert "invalid character" in res.message.lower()

    def test_string_instead_of_int(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, "1")

        assert res.status == Status.Success

    def test_None_instead_of_int(self, repo_stub):
        res = delete_ticket_usecase(repo_stub, None)

        assert res.status == Status.Error
        assert "not" in res.message.lower()
        assert "nonetype" in res.message.lower()

