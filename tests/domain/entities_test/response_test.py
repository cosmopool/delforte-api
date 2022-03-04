import pytest
from zione.core.enums import Status
from zione.domain.entities.response import Response


def test_response_object_is_instantiated():
    res = Response(Status.Success, 200)

    assert res.status == Status.Success

def test_default_value_when_no_result_paramter_given():
    res = Response(Status.Success, 200)

    assert res.result == []

def test_default_value_when_no_message_paramter_given():
    res = Response(Status.Success, 200)

    assert res.message == ""

def test_default_value_when_no_error_paramter_given():
    res = Response(Status.Success, 200)

    assert res.error == None

def test_to_dict_method_returns_dict_and_http_code():
    _, code = Response(Status.Success, 200).to_dict()

    # assert isinstance(res, Response)
    assert isinstance(code, int)

def test_to_dict_keys_is_capitalized():
    res, _ = Response(Status.Success, 200).to_dict()

    assert res['Status'] == Status.Success
    assert res['Result'] == []
    assert res['Message'] == ""
    assert res['Error'] == None

def test_http_code_should_not_exist_in_dict():
    res, _ = Response(Status.Success, 200).to_dict()

    with pytest.raises(KeyError):
        assert res['http_code']

def test_to_dict_non_capitalized_keys_should_not_exist():
    res, _ = Response(Status.Success, 200).to_dict()

    with pytest.raises(KeyError):
        assert res['status']
