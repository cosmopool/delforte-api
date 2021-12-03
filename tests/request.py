import requests
import json
import os

HOST = os.environ['APP_HOST']
PORT = os.environ['APP_PORT']


def get_response(endpoint, req_args):
    url = f"http://{HOST}:{PORT}/{endpoint}"
    data = json.dumps(req_args)
    token = set_token()
    if token['Status'] == "Success":
        token = f"Bearer {token['Result']}"
        header = {'content-type': 'application/json', 'Authorization': token}
    
        req = requests.get(url, data=data, headers=header)
        
        response = json.loads(req.content)

        print(f" --------- res: {response}")
        return response
    else:
        print(f" -------------- Could not connect and get a token from the api server.")
        print(f" -------------- Error: {token}")



def set_token():
    url = f"http://{HOST}:{PORT}/login"
    credentials = json.dumps({'username': 'kaio', 'password': 'kaio123'})
    type = {'content-type': 'application/json'}
    
    req = requests.get(url, data=credentials, headers=type)
    
    response = json.loads(req.content)

    return response
