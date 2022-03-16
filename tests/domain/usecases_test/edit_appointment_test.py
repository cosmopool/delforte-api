from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.entities.appointment import Appointment
from zione.domain.usecases.edit_appointment import edit_appointment_usecase



class TestEditAppointmentUsecase:
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
        id = self.ap_dict['id']
        res = edit_appointment_usecase(repo_stub, self.ap_dict, id)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_status_success(self, repo_stub):
        ap_dict = self.ap_dict
        id = self.ap_dict['id']
        if ap_dict.get("date"):
            self.ap_dict.pop("date")
        res = edit_appointment_usecase(repo_stub, self.ap_dict, id)

        assert res.status == Status.Success

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        ap_dict = self.ap.to_dict()
        id = self.ap_dict['id']
        if ap_dict.get("id"):
            self.ap_dict.pop("id")
        res = edit_appointment_usecase(repo_stub, ap_dict, id)

        assert res.http_code == 200

    def test_dict_with_only_one_field_should_return_status_success(self, repo_stub):
        ap_dict = {"id": 1, "date": "05-10-2021"}
        id = ap_dict['id']
        res = edit_appointment_usecase(repo_stub, ap_dict, id)

        assert res.status == Status.Success

