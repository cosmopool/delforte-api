import pytest

from .request import get_response as get

def test_open_ticket_with_all_fields():
    json = { 
            "client_name": "Mike Wazowski",
            "client_address": "Monsters, Inc. F5, Monster World",
            "client_phone": "41",
            "service_type": "Manutencao",
            "description": "Manutencao nos cilindros de grito.",
            "is_finished": "false"
            }
    expected_res = { "Status": "Success", "Result": "Ticket Opened" }
    response = get("tickets", json)

    assert response == expected_res



def test_open_ticket_with_negative_id():
    pass


# def test_open_ticket_with_client_name_field_missing():
def test_open_ticket_with_field_missing_client_name():
    pass


def test_open_ticket_with_field_missing_client_address():
    pass


def test_open_ticket_with_field_missing_client_phone():
    pass


def test_open_ticket_with_field_missing_service_type():
    pass


def test_open_ticket_with_field_missing_description():
    pass


