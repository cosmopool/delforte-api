from db import insert, auth_user
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

from .model import UserSchema
from api.response.view import handle_auth_request

class UserAuthenticate(Resource):
    def get(self):
        query_type = auth_user
        table = "users"
        schema = UserSchema

        return handle_auth_request(query_type, table, schema, create_access_token)

        # schema = UserSchema()
        # try:
        #     credentials = schema.load(request.json)
        #     # print(f"--------------------------- credentials: {credentials}")
        # except Exception as e:
        #     message = "Error"
        #     result = str(e)
        #     http_status = 406
        # else:
        #     try:
        #         result = auth_user("users", credentials)
        #     except Exception as e:
        #         message = "Error"
        #         result = ["Something went wrong while login", e]
        #         http_status = 500
        #     else:
        #         message = "Success"
        #         result = create_access_token(identity=result[0].get("username"))
        #         http_status = 200
        # finally:
        #     return {"Status": message, "Result": result}, http_status

class User(Resource):
    @jwt_required()
    def post(self):
        schema = UserSchema()

        try:
            user = schema.load(request.json)
        except Exception as e:
            print(e)
            raise Exception(e)
        else:
            result = insert_user("users", user)
            return result

    @jwt_required()
    def get(self):
        result = auth_user(user_id=2)
        return result

class Users(Resource):
    @jwt_required()
    def get(self, user_id):
        try:
            result = auth_user(user_id=user_id)
        except Exception as e:
            print(e)
            raise Exception(e)
        else:
            return result
