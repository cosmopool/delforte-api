from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.appointment import Appointment
from zione.domain.usecases.add_appointment import add_appointment_usecase

from tests.stubs.repository_stub import RepositoryStub


class TestAddAppointmentUsecase:
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

    repository = RepositoryStub()

    def test_usecase_return_response_instance(self):
        res = add_appointment_usecase(self.repository, self.ap_dict)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_http_code_406(self):
        ap_dict = self.ap_dict
        if ap_dict.get("date"):
            self.ap_dict.pop("date")
        res = add_appointment_usecase(self.repository, self.ap_dict)

        assert res.http_code == 406

    def test_dict_with_missings_fields_should_return_error(self):
        ap_dict = self.ap_dict
        if ap_dict.get("date"):
            self.ap_dict.pop("date")
        res = add_appointment_usecase(self.repository, self.ap_dict)

        assert res.error == MissingFieldError()

    def test_dict_with_missings_fields_should_return_message(self):
        ap_dict = self.ap_dict
        if ap_dict.get("date"):
            self.ap_dict.pop("date")
        res = add_appointment_usecase(self.repository, self.ap_dict)

        assert res.message == "{'date': ['Missing data for required field.']}"

    def test_dict_with_missings_fields_should_return_status_error(self):
        ap_dict = self.ap_dict
        if ap_dict.get("date"):
            self.ap_dict.pop("date")
        res = add_appointment_usecase(self.repository, self.ap_dict)

        assert res.status == Status.Error

    def test_valid_dict_should_return_http_cod_200(self):
        ap_dict = self.ap.to_dict()
        if ap_dict.get("id"):
            self.ap_dict.pop("id")
        res = add_appointment_usecase(self.repository, ap_dict)

        assert res.http_code == 200

    # def test_dict_with_missings_fields_should_return_http_code_406(self):
    #     pass
