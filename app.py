from flask import Flask, request, jsonify, make_response
import appointments.server_config as CONFIG
import os

app = Flask(__name__)

CONFIG.endpoint = "login"
BASE_URL = CONFIG.API_URL
URL = CONFIG.API_URL

@app.route('/v1/login')
def login():

    # if username == "kaio" and password == "mypass":
    #     return jsonify({ "message" : "OK", "api-token": "test_token" })
    # else:
    #     return "Send login info."

    # from ipdb import set_trace; set_trace()
    auth = request.authorization

    if auth and auth.password == "mypass":
        response = make_response('Successfull login', 200, { 'api-token': 'test_00019' })
        #from ipdb import set_trace; set_trace()
        return response

  
    #from ipdb import set_trace; set_trace()
    return make_response('Invalid credentials', 401, { 'WWW-Authenticate' : 'Basic realm="Login required"' })

if __name__ == '__main__':
    app.run()
