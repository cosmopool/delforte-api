from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
<<<<<<< HEAD

from .model import AppointmentSchema
from zione.db import select
from zione.response.view import handle_request
=======
import json

from zione.db import select, insert
from zione.appointments.model import AppointmentSchema
from zione.tickets.model import TicketSchema
from zione.response.view import handle_request, handle_request_with_schema
>>>>>>> feature/address-geocoding

class Agenda(Resource):
    @jwt_required()
    def get(self):
        query_type = select
<<<<<<< HEAD
        table = ("appointments", "tickets")
        query_vals = {"is_finished": "= false"}

        return handle_request(query_type, table, query_vals)
=======
        table = ("entry")
        query_vals = {"isFinished": "= false"}

        return handle_request(query_type, table, query_vals)

    def post(self):
        data = json.loads(request.data)
        ticket = {
                'clientName': data['clientName'],
                'clientAddress': data['clientAddress'],
                'clientPhone': data['clientPhone'],
                'serviceType': data['serviceType'],
                'description': data['description']
                }

        appointment = {
                'date': data['date'],
                'time': data['time'],
                'duration': data['duration']
                }

        if not appointment['date'] or not appointment['time'] or not appointment['duration']:
            return {'Status': 'Error', 'Result': 'Appointment with empty fields'}, 406

        ticket_schema = handle_request_with_schema(ticket, insert, 'tickets', TicketSchema, schema_partial=True)

        appointment['ticketId'] = ticket_schema[0]['Result']
        return handle_request_with_schema(appointment, insert, 'appointments', AppointmentSchema, schema_partial=True)
>>>>>>> feature/address-geocoding
