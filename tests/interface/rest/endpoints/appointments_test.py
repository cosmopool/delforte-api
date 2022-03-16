import logging
import pytest


endpoint = "/appointments"

@pytest.mark.functional
def test_fetch_appointments_entry(client, headers):
    res = client.get(endpoint, headers=headers)

    assert res.status_code == 200

@pytest.mark.functional
def test_fetch_appointments_entry_returns_entries(client, headers):

    res = client.get(endpoint, headers=headers)
    result = res.json['Result']

    assert result[0]['id'] > 0

@pytest.mark.functional
def test_add_appointments_entry_with_valid_fields(client, ap, headers):
    res = client.post(endpoint, headers=headers, json=ap)
    status = res.json['Status']
    result = res.json['Result'][0]

    assert status == "Success"
    assert result > 0

@pytest.mark.functional
def test_add_appointments_entry_with_missing_appointment_fields(client, ap, headers, caplog):
    caplog.set_level(logging.DEBUG)
    ap.pop('date')
    res = client.post(endpoint, headers=headers, json=ap)
    status = res.json['Status']
    result = res.json['Result'].lower()

    assert status == "Error"
    assert "missing" in result and "field" in result

@pytest.mark.functional
def test_add_appointments_entry_with_invalid_appointment_schema_fields(client, ap, headers):
    ap['isFinished'] = "invalid"
    res = client.post(endpoint, headers=headers, json=ap)
    status = res.json['Status']
    result = res.json['Result'].lower()

    assert status == "Error"
    assert "not a valid" in result


class TestFetchAppointment:
    @pytest.mark.functional
    def test_fetch_appointment_with_valid_id(self, client, headers):
        _endpoint = f"{endpoint}/1"
        res = client.get(_endpoint, headers=headers)
        status = res.json['Status']

        assert status == "Success"

    @pytest.mark.functional
    def test_fetch_appointment_with_valid_id_1(self, client, ap, headers):
        _endpoint = f"{endpoint}/1"
        res = client.get(_endpoint, headers=headers)
        result = res.json['Result'][0]

        assert result['ticketId'] == ap['ticketId']

    @pytest.mark.functional
    def test_fetch_appointment_with_valid_id_4(self, client, ap, headers):
        _endpoint = f"{endpoint}/3"
        res = client.get(_endpoint, headers=headers)
        result = res.json['Result'][0]
        logging.debug(f"res from patch: {res.json['Result']}")

        assert result['ticketId'] == ap['ticketId']

    @pytest.mark.functional
    def test_fetch_appointment_with_invalid_id_negative(self, client, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.get(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_fetch_appointment_with_invalid_id_string(self, client, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.get(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_fetch_appointment_with_invalid_id_sql_injection(self, client, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.get(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestEditAppointment:
    endpoint = f"{endpoint}/3"
    
    @pytest.mark.functional
    def test_edit_appointment_with_valid_id(self, client, ap, headers):
        ap['date'] = "2021-01-01"
        res = client.patch(self.endpoint, headers=headers, json=ap)
        status = res.json['Status']

        assert status == "Success"

    @pytest.mark.functional
    def test_edit_appointment_with_valid_id_3(self, client, ap, headers):
        new_date = "2021-03-03"
        ap['date'] = new_date
        _endpoint = f"{endpoint}/3"

        res_patch = client.patch(_endpoint, headers=headers, json=ap)
        res_get = client.get(_endpoint, headers=headers)
        status = res_patch.json['Status']
        result = res_get.json['Result'][0]
        logging.debug(f"res from patch: {res_patch.json['Result']}")
        logging.debug(f"res from get: {res_get.json['Result']}")

        assert status == "Success"
        assert result['date'] == new_date

    @pytest.mark.functional
    def test_edit_appointment_with_invalid_id_negative(self, client, ap, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.patch(_endpoint, headers=headers, json=ap)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_edit_appointment_with_invalid_id_string(self, client, ap, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.patch(_endpoint, headers=headers, json=ap)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_edit_appointment_with_invalid_id_sql_injection(self, client, ap, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.patch(_endpoint, headers=headers, json=ap)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestDeleteAppointment:
    endpoint = f"{endpoint}/1"

    @pytest.mark.functional
    def test_delete_appointment_with_valid_id(self, client, headers, add_ap):
        appointment_id = add_ap
        _endpoint = f"{endpoint}/{appointment_id}"
        res = client.delete(_endpoint, headers=headers)
        status = res.json['Status']

        res_get = client.get(_endpoint, headers=headers)
        result = res_get.json['Result']

        assert status == "Success"
        assert "no record found with given id" in result.lower()

    @pytest.mark.functional
    def test_delete_appointment_with_invalid_id_negative(self, client, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_delete_appointment_with_invalid_id_string(self, client, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_delete_appointment_with_invalid_id_sql_injection(self, client, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestCloseAppointment:
    def __endpoint__(self, id: int) -> str:
        return f"{endpoint}/{id}/actions/close"

    @pytest.mark.functional
    def test_close_appointment_with_valid_id(self, client, headers, caplog):
        caplog.set_level(logging.DEBUG)
        ap_id = 1
        _endpoint = self.__endpoint__(ap_id)
        res = client.post(_endpoint, headers=headers)
        status = res.json['Status']

        res_get = client.get(f"appointments/{ap_id}", headers=headers)
        ap = res_get.json['Result'][0]

        assert status == "Success"
        assert ap['isFinished'] == True

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_negative(self, client, headers, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post(f"appointments/{-5}/actions/close", headers=headers)
        logging.debug(f"[PYTEST] res: {res.json}")
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_string(self, client, headers, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post("appointments/a8/actions/close", headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_sql_injection(self, client, headers, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post("appointments/ or 1=1;–/actions/close", headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestRescheduleAppointment:
    def __endpoint__(self, id: int) -> str:
        return f"{endpoint}/{id}/actions/reschedule"

    @pytest.mark.functional
    def test_reschedule_appointment_with_valid_id(self, client, ap, headers, caplog):
        caplog.set_level(logging.DEBUG)
        ap['duration'] = "20:00"
        ap_id = 1
        _endpoint = self.__endpoint__(ap_id)
        res = client.post(_endpoint, headers=headers, json=ap)
        status = res.json['Status']

        res_get = client.get(f"appointments/{ap_id}", headers=headers)
        _ap = res_get.json['Result'][0]

        assert status == "Success"
        assert _ap['duration'] == "20:00:00"

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_negative(self, client, headers, ap, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post(f"appointments/{-5}/actions/reschedule", headers=headers, json=ap)
        logging.debug(f"[PYTEST] res: {res.json}")
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_string(self, client, headers, ap, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post("appointments/a8/actions/reschedule", headers=headers, json=ap)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_appointment_with_invalid_id_sql_injection(self, client, headers, ap, caplog):
        caplog.set_level(logging.DEBUG)
        res = client.post("appointments/ or 1=1;–/actions/reschedule", headers=headers, json=ap)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result
