import os

endpoint = ""
API_VERSION = os.environ.get("API_VERSION")
BASE_URL = os.environ.get("BASE_URL")
API_URL = f"{BASE_URL}v{API_VERSION}/{endpoint}/"
