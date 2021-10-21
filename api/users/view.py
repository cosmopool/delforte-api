from db import insert, select, delete, update, auth_user
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from .model import UserSchema

class UserAuthenticate(Resource):
    def get(self):
        schema = UserSchema()
        credentials = schema.load(request.json)

        try:
            result = auth_user("users", credentials)
        except:
            message = "message"
            result = "Something went wrong while login"
            http_status = 500
        else:
            message = "access token"
            result = create_access_token(identity=result[0].get("username"))
            http_status = 200
        finally:
            return {message: result}, http_status

    def __authentication__(self, user):
        pass
    
    def __identity__(self):
        pass

class User(Resource):
    @jwt_required()
    def post(self):
        schema = UserSchema()
        user = schema.load(request.json)

        result = insertUser("users", user)
        return result

    @jwt_required()
    def get(self):
        result = auth_user(user_id=2)
        return result

class Users(Resource):
    @jwt_required()
    def get(self, user_id):
        result = auth_user(user_id=user_id)
        return result