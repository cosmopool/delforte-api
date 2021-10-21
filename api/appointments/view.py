from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from db import insert, select, delete, update
from .model import AppointmentSchema

class AppointmentOpen(Resource):
    @jwt_required()
    def get(self):
        try:
            result = select("appointments", {"is_finished": "false"})
        except:
            message = "Error"
            result = "Something went wrong while searching your data"
            http_status = 500
        else:
            message = "Open Appointments"
            http_status = 200
        finally:
            return {message: result}, http_status

    @jwt_required()
    def post(self):
        """ Book a new appointment """
        schema = AppointmentSchema()
        appointment = schema.load(request.json)

        try:
            result = insert("appointments", appointment)
        except:
            message = "Error"
            result = "Something went wrong while searching your data"
            http_status = 500
        else:
            message = "Appointment booked"
            http_status = 200
        finally:
            return {message: result}, http_status

class Appointments(Resource):
    @jwt_required()
    def get(self, appointment_id):
        """ Get information about specific appointment """
        try:
            result = select("appointments", {"id": appointment_id})
        except:
            message = "Error"
            result = "Something went wrong while searching your data"
            http_status = 500
        else:
            message = "Appointment"
            http_status = 200
        finally:
            return {message: result}, http_status

    @jwt_required()
    def patch(self,appointment_id):
        """ Edit a specific appointment """
        pass

    @jwt_required()
    def delete(self,appointment_id):
        """ Delete a specific appointment """
        pass

class AppointmentsActionsClose(Resource):
    @jwt_required()
    def post(self,appointment_id):
        """ Close a open appointment """
        pass

class AppointmentsActionsReschedule(Resource):
    @jwt_required()
    def post(self,appointment_id):
        """ Reschedule a specific appointment to a new date """
        pass
