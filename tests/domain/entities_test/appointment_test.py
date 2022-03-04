import pytest

from zione.domain.entities.appointment import Appointment

class TestAppointmentInstance:
    ap_dict = {"id": 1, "time": "10:00", "date": "12-12-2021", "duration": "1:00", "ticketId": 1, "isFinished": False}
    ap = Appointment(id = 1, time = "10:00", date = "12-12-2021", duration = "1:00", ticketId = 1, isFinished = False)

    def test_appointment_entity_init(self):
        assert self.ap.id == 1
        assert self.ap.time == "10:00"
        assert self.ap.date == "12-12-2021"
        assert self.ap.duration == "1:00"
        assert self.ap.ticketId == 1
        assert self.ap.isFinished == False

    def test_appointment_entity_to_dict(self):
        assert self.ap.to_dict() == self.ap_dict
        self.ap

    # def test_appointment_entity_to_dict_keys_is_in_camel_case(self):
    #     d = self.ap.to_dict()
    #
    #     assert d["ticketId"] is not None
    #     assert d["isFinished"] is not None

    def test_appointment_entity_from_dict(self):
        ap = Appointment.from_dict(self.ap_dict)
        
        assert ap.id == 1
        assert ap.time == "10:00"
        assert ap.date == "12-12-2021"
        assert ap.duration == "1:00"
        assert ap.ticketId == 1
        assert ap.isFinished == False

    def test_appointment_entity_comparison(self):
        ap1 = self.ap
        ap2 = Appointment.from_dict(self.ap_dict)

        assert ap1 == ap2

    def test_appointment_entity_to_dict_with_additional_fields(self):
        additonal_field = {
        "id": 1,
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "client_name": "Roberto Barao",
        "client_address": "Rua David Campista, 211",
        "client_phone": 41999000888,
        "service_type": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
        }
        ap = Appointment.from_dict(additonal_field)

        assert ap == self.ap

    def test_appointment_entity_to_dict_with_missing_fields(self):
        missing_field = {"id": 1, "ticketId": 1, "isFinished": False}

        with pytest.raises(TypeError):
            _ = Appointment.from_dict(missing_field)

    def test_appointment_entity_from_dict_id_default_value(self):
        ap_no_id = {
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "client_name": "Roberto Barao",
        "client_address": "Rua David Campista, 211",
        "client_phone": 41999000888,
        "service_type": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
        }
        ap = Appointment.from_dict(ap_no_id)

        assert ap.id == -1

    # def test_appointment_entity_default_id_value(self):
    #     ap_no_id = {
    #     "time": "10:00",
    #     "date": "12-12-2021",
    #     "duration": "1:00",
    #     "ticketId": 1,
    #     "isFinished": False
    #     }
    #     ap = Appointment.from_dict(ap_no_id)
    #     ap_dict = ap.to_dict()
    #
    #     assert ap_dict['id'] == -1
    #
    # def test_appointment_entity_to_dict_should_have_no_id_if_id_less_equal_then_0(self):
    #     ap_no_id = {
    #     "time": "10:00",
    #     "date": "12-12-2021",
    #     "duration": "1:00",
    #     "ticketId": 1,
    #     "client_name": "Roberto Barao",
    #     "client_address": "Rua David Campista, 211",
    #     "client_phone": 41999000888,
    #     "service_type": "Manutencao",
    #     "description": "Alarme nao arma",
    #     "isFinished": False
    #     }
    #     ap = Appointment.from_dict(ap_no_id)
    #     ap_dict = ap.to_dict()
    #
    #     assert ap_dict.get('id') == None

    # def test_appointment_entity_from_dict_should_error_on_empty_field(self):
    #     ap_no_id = {
    #     "id": None,
    #     "time": "10:00",
    #     "date": "12-12-2021",
    #     "duration": "1:00",
    #     "ticketId": 1,
    #     "isFinished": False
    #     }
    #     ap = Appointment.from_dict(ap_no_id)
    #     ap_dict = ap.to_dict()
    #
    #     assert ap_dict['id'] == -1


    def test_user_entity_endpoint_value(self):
        endpoint = Appointment.endpoint

        assert endpoint == "appointments"
