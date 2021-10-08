import os
import pytest
import authentication.basic_authentication as Auth

# TODO: check if there is api_key value in header

def test_check_api_is_valid():
    """ Basic implementation of authentication. """
    # TODO: implement a better authentication check
    assert Auth.is_authenticated() == True
