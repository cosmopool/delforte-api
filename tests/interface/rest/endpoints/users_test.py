import logging
import pytest


endpoint = "/login"

@pytest.mark.functional
def test_user_authentication_on_valid_credentials(client, user):
    res = client.post(endpoint, json=user)
    result = res.json['Result'][0]

    assert res.status_code == 200
    assert len(result) > 50

@pytest.mark.functional
def test_user_authentication_on_invalid_character_credentials_username(client, user):
    user['username'] = "aaaaa"
    res = client.post(endpoint, json=user)
    result = res.json['Result'][0]
    status = res.json['Status']

    assert res.status_code == 401
    assert status == "Error"
    assert len(result) > 0

@pytest.mark.functional
def test_user_authentication_on_invalid_character_credentials_password(client, user):
    user['password'] = "aaaaa"
    res = client.post(endpoint, json=user)
    result = res.json['Result'][0]
    status = res.json['Status']

    assert res.status_code == 401
    assert status == "Error"
    assert len(result) > 0

@pytest.mark.functional
def test_user_authentication_with_missing_username_field(client, user):
    user.pop('username')
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 406
    assert status == "Error"
    assert "missing" in result.lower()
    assert "field" in result.lower()

def test_user_authentication_with_missing_password_field(client, user):
    user.pop('password')
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 406
    assert status == "Error"
    assert "missing" in result.lower()
    assert "field" in result.lower()

def test_sql_injection_with_single_double_quote(client, user):
    user['username'] = "\""
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 412
    assert status == "Error"
    assert "invalid character" in result.lower()

def test_sql_injection_2(client, user):
    user['username'] = "kaio’ or ‘x’=’x"
    user['password'] = "asdfasdf"
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 412
    assert status == "Error"
    assert "invalid character" in result.lower()

def test_sql_injection_1(client, user):
    user['username'] = " or 1=1;–"
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 412
    assert status == "Error"
    assert "invalid character" in result.lower()

def test_sql_injection_drop_table(client, user, caplog):
    caplog.set_level(logging.DEBUG)
    user['username'] = "kaio’; DROP table users;’—"
    res = client.post(endpoint, json=user)
    result = res.json['Result']
    status = res.json['Status']

    assert res.status_code == 412
    assert status == "Error"
    assert "invalid character" in result.lower()

