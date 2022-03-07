from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.usecases.fetch_open_appointments import fetch_open_appointments_usecase


class TestEditAppointmentUsecase:
    ap_dict = {
        "id": 1,
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "isFinished": False,
    }


    def test_usecase_return_response_instance(self, repo_stub):
        res = fetch_open_appointments_usecase(repo_stub)

        assert isinstance(res, Response)

    def test_should_return_status_success(self, repo_stub):
        res = fetch_open_appointments_usecase(repo_stub)

        assert res.status == Status.Success

    def test_sould_return_open_appointment_in_result(self, repo_stub):
        res = fetch_open_appointments_usecase(repo_stub)

        assert res.result == [self.ap_dict.__str__()]

