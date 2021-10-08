import os
import pytest
from authentication import basic_autentication as Auth


def test_check_api_key_on_request_header():
    assert Auth.is_authenticated == 1
