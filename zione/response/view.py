<<<<<<< HEAD
from flask import request

def handle_request_with_schema(query_type, table, schema, schema_partial=False, msg_ok="Success", query_vals=None, err_code=409, req=request):
=======
# from zione.request.view import address_geocoding

def parse_json_schema(schema, json, schema_partial):
    schema_view = schema(partial=schema_partial)
    message = "Success"

    try:
        result = schema_view.load(json)
    except Exception as e:
        message = "Error"
        result = f"Error parsing JSON: {str(e)}"
        http_status = 406
    finally:
        return {"Status": message, "Result": result}


def handle_request_with_schema(req_json, query_type, table, schema, schema_partial=False, msg_ok="Success", query_vals=None, err_code=409):
>>>>>>> feature/address-geocoding
    """


    :param query_type:
    :param table:
    :param schema:
    :param msg_ok:
    :param req:
    """
<<<<<<< HEAD
    schema_view = schema(partial=schema_partial)
    try:
        data_from_request = schema_view.load(req.json)
    except Exception as e:
        message = "Error"
        result = f"Error parsing JSON: {str(e)}"
        http_status = 406
    else:
        try:
            if query_vals:
                result = query_type(table, data_from_request, query_vals)
            else:
                result = query_type(table, data_from_request)
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 500
        else:
            message = msg_ok
            http_status = 200
=======
    data_from_request = parse_json_schema(schema, req_json, schema_partial)
    if data_from_request['Status'] == 'Error':
        return {"Status": data_from_request['Status'], "Result": data_from_request['Result']}, 500

    try:
        if query_vals:
            result = query_type(table, data_from_request['Result'], query_vals)
        else:
            result = query_type(table, data_from_request['Result'])
    except Exception as e:
        message = "Error"
        result = str(e)
        http_status = 500
    else:
        message = msg_ok
        http_status = 200
>>>>>>> feature/address-geocoding
    finally:
        return {"Status": message, "Result": result}, http_status

def handle_request(query_type, table, query_vals, msg_ok="Success", http_status_err=500):
    """

    :param query_type: function from db.py to interact with postgres database, it can be: insert, update, delete, etc...
    :param table: what table from postgres database to update.
    :param http_status_err: when something goes wrong with the given query, wich http status we send to the user?
    """
    try:
        result = query_type(table, query_vals)
    except Exception as err:
        message = "Error"
        result = str(err)
        http_status = http_status_err
    else:
        message = msg_ok
        http_status = 200
    finally:
        return {"Status": message, "Result": result}, http_status

<<<<<<< HEAD
def handle_auth_request(query_type, table, schema, create_token_callback):
        try:
            credentials = schema().load(request.json)
=======
def handle_auth_request(req_json, query_type, table, schema, create_token_callback):
        try:
            credentials = schema().load(req_json)
>>>>>>> feature/address-geocoding
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 406
        else:
            try:
                result = query_type(table, credentials)
            except Exception as e:
                message = "Error"
                result = ["Something went wrong while login", str(e)]
                http_status = 500
            else:
                message = "Success"
                result = create_token_callback(identity=result[0].get("username"))
                http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status
