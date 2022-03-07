from zione.core.enums import Status
from zione.core.exceptions import InvalidValueError
from zione.domain.entities.response import Response
from zione.domain.entities.appointment import Appointment
from zione.domain.usecases.close_appointment import close_appointment_usecase



class TestCloseAppointmentUsecase:
    ap = Appointment(
        id=1,
        time="10:00",
        date="12-12-2021",
        duration="1:00",
        ticketId=1,
        isFinished=False,
    )
    ap_dict = {
        "id": 1,
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "isFinished": False,
    }


    def test_usecase_return_response_instance(self, repo_stub):
        res = close_appointment_usecase(repo_stub, self.ap.id)

        assert isinstance(res, Response)

    def test_invalid_id_number(self, repo_stub):
        res = close_appointment_usecase(repo_stub, -4)

        assert res.status == Status.Error
        assert res.http_code == 406

    def test_string_instead_of_int(self, repo_stub):
        res = close_appointment_usecase(repo_stub, "1")

        assert res.error == InvalidValueError()
        assert "Invalid field value" in res.message

    def test_None_instead_of_int(self, repo_stub):
        res = close_appointment_usecase(repo_stub, None)

        assert res.status == Status.Error
        assert "Invalid field value" in res.message

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        res = close_appointment_usecase(repo_stub, self.ap.id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub):
        res = close_appointment_usecase(repo_stub, self.ap.id)

        assert res.status == Status.Success

