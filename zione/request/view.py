from flask import request
import requests
import json
import urllib.parse

def parse_req_to_json(schema, callback, req=request):
    schema_model = schema()
    try:
        data_from_request = schema_model.load(req.json)
    except Exception as e:
        message = "Error"
        result = str(e)
        http_status = 406
        res = make_api_response(message, result, http_status)
    else:
        res = callback
    finally:
        return res

def make_api_response(msg, res, code):
    return {"Status": msg, "res": res}, code

def address_geocoding(address):
    # TODO: use google geocoding api
    address_encoded = urllib.parse.quote(address)
    url = f"http://api.positionstack.com/v1/forward?access_key=e35984b52f301530ccef88aa2260179e&output=json&query={address_encoded}"

    req = requests.get(url)
    res = json.loads(req.content)

    return res
