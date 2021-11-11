from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from db import insert, select, delete, update
from .model import AppointmentSchema

class Agenda(Resource):
    @jwt_required()
    def get(self):
        try:
            result = select(("appointments", "tickets"), {"is_finished": "= false"})
        except Exception as e:
            message = "Error"
            result = ["Something went wrong while searching your data", e]
            http_status = 500
        else:
            message = "Agenda"
            http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

