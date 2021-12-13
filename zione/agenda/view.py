from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json

from zione.db import select, insert
from zione.appointments.model import AppointmentSchema
from zione.tickets.model import TicketSchema
from zione.response.view import handle_request, handle_request_with_schema

class Agenda(Resource):
    @jwt_required()
    def get(self):
        query_type = select
        table = ("entry")
        query_vals = {"isFinished": "= false"}

        return handle_request(query_type, table, query_vals)

    def post(self):
        appointment_json_with_ticket_id = json.loads(request.data)

        ticket_schema = handle_request_with_schema(request.json, insert, 'tickets', TicketSchema)

        appointment_json_with_ticket_id['ticketId'] = ticket_schema[0]['Result']
        return handle_request_with_schema(appointment_json_with_ticket_id, insert, 'appointments', AppointmentSchema)
