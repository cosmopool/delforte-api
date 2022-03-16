import logging

from zione.core.enums import Status
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
        assert res.http_code == 412

    def test_invalid_string(self, repo_stub):
        res = close_appointment_usecase(repo_stub, "a")
        print(res)

        assert res.status == Status.Error
        assert "invalid character" in res.message.lower()

    def test_send_integer_as_string(self, repo_stub):
        res = close_appointment_usecase(repo_stub, "1")

        assert res.status == Status.Success

    def test_None_instead_of_int(self, repo_stub, caplog):
        caplog.set_level(logging.DEBUG)
        res = close_appointment_usecase(repo_stub, None)

        assert res.status == Status.Error
        assert "not" in res.message.lower()
        assert "nonetype" in res.message.lower()

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        res = close_appointment_usecase(repo_stub, self.ap.id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub):
        res = close_appointment_usecase(repo_stub, self.ap.id)

        assert res.status == Status.Success

