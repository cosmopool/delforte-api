import pytest
import requests
import os
from ipdb import set_trace
#import appointments.server_config as Config

ENDPOINT = "login"
API_VERSION = os.environ.get("API_VERSION")
BASE_URL = os.environ.get("BASE_URL")
#API_URL = f"{BASE_URL}v{API_VERSION}/{ENDPOINT}/"
API_URL = "http://localhost:5000/v1/login"

class TestLogin():
    # def test_checl_if_route_exists():
    #     response = requests.get()

    def test_check_if_route_exist(self):
        response = requests.get(API_URL)
        status_code = response.status_code

        assert status_code != 404

    def test_check_if_credential_are_valid(self):
        username = "kaio"
        password = "mypass"
        response = requests.get(API_URL, auth=(username, password))
        
        assert response.status_code == 200

    def test_check_if_credential_are_valid_to_return_access_token(self):
        username = "kaio"
        password = "mypass"
        response = requests.get(API_URL, auth=(username, password))

        assert response.headers['api-token'] == 'test_00019'
