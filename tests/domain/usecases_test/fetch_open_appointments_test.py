from zione.core.enums import Status
from zione.domain.entities.response import Response
from zione.domain.usecases.fetch_appointment import fetch_appointment_usecase

from tests.stubs.repository_stub import RepositoryStub


class TestEditAppointmentUsecase:
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
        res = fetch_appointment_usecase(self.repository, 1)

        assert isinstance(res, Response)

    def test_should_return_status_success(self):
        res = fetch_appointment_usecase(self.repository, 1)

        assert res.status == Status.Success

    def test_sould_return_open_appointment_in_result(self):
        res = fetch_appointment_usecase(self.repository, 1)

        assert res.result == [self.ap_dict.__str__()]

