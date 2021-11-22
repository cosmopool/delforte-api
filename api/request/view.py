from flask import request

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
