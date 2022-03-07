from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.usecases.delete_appointment import delete_appointment_usecase


class TestDeleteAppointmentUsecase:

    def test_return_response_instance(self, repo_stub):
        res = delete_appointment_usecase(repo_stub, 1)

        assert isinstance(res, Response)

    def test_valid_id_number(self, repo_stub):
        res = delete_appointment_usecase(repo_stub, 1)

        assert isinstance(res, Response)

    def test_invalid_id_number(self, repo_stub):
        res = delete_appointment_usecase(repo_stub, -4)

        assert res.status == Status.Error
        assert res.http_code == 406

    def test_string_instead_of_int(self, repo_stub):
        res = delete_appointment_usecase(repo_stub, "1")

        assert res.error == InvalidValueError()
        assert "Invalid field value" in res.message

    def test_None_instead_of_int(self, repo_stub):
        res = delete_appointment_usecase(repo_stub, None)

        assert res.status == Status.Error
        assert "Invalid field value" in res.message

