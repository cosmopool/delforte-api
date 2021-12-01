import requests
import json
import os

HOST = os.environ['APP_HOST']
PORT = os.environ['APP_PORT']


def get_response(endpoint, req_args):
    url = f"http://{HOST}:{PORT}/{endpoint}"
    credentials = json.dumps(req_args)
    type = {'content-type': 'application/json'}
    
    req = requests.get(url, data=credentials, headers=type)
    
    response = json.loads(req.content)

    return response
