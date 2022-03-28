import logging
import pytest


endpoint = "/agenda"

@pytest.mark.functional
def test_fetch_agenda_entry2(client, headers):
    res = client.get("/agenda", headers=headers)

    assert res.status_code == 200

@pytest.mark.functional
def test_fetch_agenda_entry(client, headers):
    res = client.get(endpoint, headers=headers)

    assert res.status_code == 200

@pytest.mark.functional
def test_fetch_agenda_entry_returns_entries(client, headers, caplog):
    caplog.set_level(logging.DEBUG)

    res = client.get(endpoint, headers=headers)
    result = res.json['Result']

    assert result[0]['id'] > 0

@pytest.mark.functional
def test_add_agenda_entry_with_valid_fields(client, ag, headers):
    res = client.post(endpoint, json=ag, headers=headers)
    print(res)
    status = res.json['Status']

    assert status == "Success"

@pytest.mark.functional
def test_add_agenda_entry_with_missing_ticket_fields(client, ag, headers):
    ag.pop('clientName')
    res = client.post(endpoint, json=ag, headers=headers)
    status = res.json['Status']
    result = res.json['Result']

    assert status == "Error"
    assert "error saving ticket." in result.lower()

@pytest.mark.functional
def test_add_agenda_entry_with_missing_appointment_fields(client, ag, caplog, headers):
    caplog.set_level(logging.DEBUG)
    ag.pop('date')
    res = client.post(endpoint, json=ag, headers=headers)
    status = res.json['Status']
    result = res.json['Result']
    logging.debug(f"response: {res}")

    assert status == "Error"
    assert "error saving appointment." in result.lower()

@pytest.mark.functional
def test_add_agenda_entry_with_invalid_ticket_schema_fields(client, ag, headers):
    ag['isFinished'] = "invalid"
    res = client.post(endpoint, json=ag, headers=headers)
    status = res.json['Status']
    result = res.json['Result']

    assert status == "Error"
    assert "error saving ticket." in result.lower()
    assert "not a valid" in result.lower()

@pytest.mark.functional
def test_add_agenda_entry_with_invalid_appointment_schema_fields(client, ag, headers):
    ag['date'] = 0
    res = client.post(endpoint, json=ag, headers=headers)
    status = res.json['Status']
    result = res.json['Result']

    assert status == "Error"
    assert "error saving appointment." in result.lower()
    assert "not a valid" in result.lower()

@pytest.mark.functional
def test_add_agenda_entry_with_invalid_appointment_fields(client, ag, caplog, headers):
    caplog.set_level(logging.DEBUG)
    ag['date'] = "16-12-2021"
    res = client.post(endpoint, json=ag, headers=headers)
    status = res.json['Status']
    result = res.json['Result']
    logging.debug(f"response: {res}")

    assert status == "Error"
    assert "error saving appointment." in result.lower()
