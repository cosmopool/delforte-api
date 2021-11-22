from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

# from db import insert, select, delete, update
from db import select
from .model import AppointmentSchema
from api.response.view import handle_request

class Agenda(Resource):
    @jwt_required()
    def get(self):
        query_type = select
        table = ("appointments", "tickets")
        query_vals = {"is_finished": "= false"}

        return handle_request(query_type, table, query_vals)
