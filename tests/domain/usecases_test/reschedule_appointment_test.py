from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.entities.appointment import Appointment
from zione.domain.usecases.reschedule_appointment import reschedule_appointment_usecase


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
        "time": "11:00",
        "date": "05-02-2022",
        "duration": "1:30",
    }

    def test_usecase_return_response_instance(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, self.ap.id)

        assert isinstance(res, Response)

    def test_invalid_id_number(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, -4)

        assert res.status == Status.Error
        assert res.http_code == 412

    def test_invalid_string(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, "a")

        assert res.status == Status.Error
        assert "invalid character" in res.message.lower()

    def test_string_instead_of_int(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, "1")

        assert res.status == Status.Success

    def test_None_instead_of_int(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, None)

        assert res.status == Status.Error
        assert "not" in res.message.lower()
        assert "nonetype" in res.message.lower()

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, self.ap.id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub):
        new_date = self.ap_dict
        new_date.pop("duration")
        new_date.pop("date")
        res = reschedule_appointment_usecase(repo_stub, new_date, self.ap.id)

        assert res.status == Status.Success

    def test_dict_with_date_time_duration_fields_should_return_status_success(self, repo_stub):
        res = reschedule_appointment_usecase(repo_stub, self.ap_dict, self.ap.id)

        assert res.status == Status.Success

    def test_dict_without_any_required_field(self, repo_stub):
        new_date = self.ap.to_dict()
        new_date.pop("duration")
        new_date.pop("date")
        new_date.pop("time")
        res = reschedule_appointment_usecase(repo_stub, new_date, self.ap.id)

        assert res.status == Status.Error
        assert "missing required fields" in res.message.lower()

