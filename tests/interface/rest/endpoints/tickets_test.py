import logging
import pytest


endpoint = "/tickets"

@pytest.mark.functional
def test_fetch_tickets_entry(client, headers):
    res = client.get(endpoint, headers=headers)
    # print(res.json['Result'])

    assert res.status_code == 200

@pytest.mark.functional
def test_fetch_tickets_entry_returns_entries(client, headers):

    res = client.get(endpoint, headers=headers)
    result = res.json['Result']

    assert result[0]['id'] > 0

@pytest.mark.functional
def test_add_tickets_entry_with_valid_fields(client, tk, headers):
    res = client.post(endpoint, headers=headers, json=tk)
    status = res.json['Status']
    result = res.json['Result'][0]

    assert status == "Success"
    assert result > 0

@pytest.mark.functional
def test_add_tickets_entry_with_missing_ticket_fields(client, tk, headers):
    tk.pop('clientName')
    res = client.post(endpoint, headers=headers, json=tk)
    status = res.json['Status']
    result = res.json['Result'].lower()

    assert status == "Error"
    assert "missing" in result and "field" in result

@pytest.mark.functional
def test_add_tickets_entry_with_invalid_ticket_schema_fields(client, tk, headers):
    tk['isFinished'] = "invalid"
    res = client.post(endpoint, headers=headers, json=tk)
    status = res.json['Status']
    result = res.json['Result'].lower()

    assert status == "Error"
    assert "not a valid" in result


class TestFetchTicket:
    @pytest.mark.functional
    def test_fetch_ticket_with_valid_id(self, client, tk, headers):
        _endpoint = f"{endpoint}/1"
        res = client.get(_endpoint, headers=headers, json=tk)
        status = res.json['Status']

        assert status == "Success"

    @pytest.mark.functional
    def test_fetch_ticket_with_valid_id_1(self, client, tk, headers):
        _endpoint = f"{endpoint}/1"
        res = client.get(_endpoint, headers=headers, json=tk)
        result = res.json['Result'][0]

        assert result['clientName'] == "Roberto Barao"

    @pytest.mark.functional
    def test_fetch_ticket_with_valid_id_4(self, client, tk, headers):
        _endpoint = f"{endpoint}/3"
        res = client.get(_endpoint, headers=headers, json=tk)
        result = res.json['Result'][0]
        logging.debug(f"res from patch: {res.json['Result']}")


        assert result['clientAddress'] == tk['clientAddress']

    @pytest.mark.functional
    def test_fetch_ticket_with_invalid_id_negative(self, client, tk, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.get(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_fetch_ticket_with_invalid_id_string(self, client, tk, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.get(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_fetch_ticket_with_invalid_id_sql_injection(self, client, tk, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.get(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestEditTicket:
    endpoint = f"{endpoint}/3"
    
    @pytest.mark.functional
    def test_edit_ticket_with_valid_id(self, client, tk, headers):
        tk['clientName'] = "Robertao da pizadinha"
        res = client.patch(self.endpoint, headers=headers, json=tk)
        status = res.json['Status']

        assert status == "Success"

    @pytest.mark.functional
    def test_edit_ticket_with_valid_id_3(self, client, tk, headers):
        new_name = "Robertinha da pizadona"
        tk['clientName'] = new_name
        _endpoint = f"{endpoint}/3"

        res_patch = client.patch(_endpoint, headers=headers, json=tk)
        res_get = client.get(_endpoint, headers=headers)
        status = res_patch.json['Status']
        result = res_get.json['Result'][0]
        logging.debug(f"res from patch: {res_patch.json['Result']}")
        logging.debug(f"res from get: {res_get.json['Result']}")

        assert status == "Success"
        assert result['clientName'] == new_name

    @pytest.mark.functional
    def test_edit_ticket_with_invalid_id_negative(self, client, tk, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.patch(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_edit_ticket_with_invalid_id_string(self, client, tk, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.patch(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_edit_ticket_with_invalid_id_sql_injection(self, client, tk, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.patch(_endpoint, headers=headers, json=tk)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestDeleteTicket:
    endpoint = f"{endpoint}/1"

    @pytest.mark.functional
    def test_delete_ticket_with_valid_id(self, client, headers, add_tk):
        ticket_id = add_tk
        _endpoint = f"{endpoint}/{ticket_id}"
        res = client.delete(_endpoint, headers=headers)
        status = res.json['Status']

        res_get = client.get(_endpoint, headers=headers)
        result = res_get.json['Result']

        assert status == "Success"
        assert "no record found with given id" in result.lower()

    @pytest.mark.functional
    def test_delete_ticket_with_invalid_id_negative(self, client, headers):
        _endpoint = f"{endpoint}/-6"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_delete_ticket_with_invalid_id_string(self, client, headers):
        _endpoint = f"{endpoint}/a8"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_delete_ticket_with_invalid_id_sql_injection(self, client, headers):
        _endpoint = f"{endpoint}/ or 1=1;–"
        res = client.delete(_endpoint, headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result


class TestCloseTicket:
    def __endpoint__(self, id: int) -> str:
        return f"{endpoint}/{id}/actions/close"

    @pytest.mark.functional
    def test_close_ticket_with_valid_id(self, client, headers):
        tk_id = 5
        _endpoint = self.__endpoint__(tk_id)
        res = client.post(_endpoint, headers=headers)
        status = res.json['Status']

        res_get = client.get(f"tickets/{tk_id}", headers=headers)
        tk = res_get.json['Result'][0]
        print(f"------------------- res_get {res_get.json}")
        print(f"------------------- tk {tk}")

        assert status == "Success"
        assert tk['isFinished'] == True

    @pytest.mark.functional
    def test_post_ticket_with_invalid_id_negative(self, client, headers):
        res = client.post(f"tickets/{-5}/actions/close", headers=headers)
        logging.debug(f"[PYTEST] res: {res.json}")
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_ticket_with_invalid_id_string(self, client, headers):
        res = client.post("tickets/a8/actions/close", headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result

    @pytest.mark.functional
    def test_post_ticket_with_invalid_id_sql_injection(self, client, headers):
        res = client.post("tickets/ or 1=1;–/actions/close", headers=headers)
        result = res.json['Result'].lower()

        assert "invalid" in result and "parameter" in result
