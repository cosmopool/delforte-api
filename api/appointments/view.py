import db
from flask_restful import Resource
from flask import request
from .model import AppointmentSchema

class AppointmentOpen(Resource):
    def post(self):
        """ Book a new appointment """
        schema = AppointmentSchema()
        appointment = schema.load(request.json)

        result = db.insert("appointments", appointment)
        return {"message": result}, 200

class Appointments(Resource):
    def get(self, appointment_id):
        """ Get information about specific appointment """
        print("hey")
        try:
            result = db.select("appointments", {"id": appointment_id})
        except:
            result = "something went wrong searching your data"
            http_status = 500
        else:
            http_status = 200
        finally:
            return result, http_status
        pass

    def patch(self,appointment_id):
        """ Edit a specific appointment """
        pass

    def delete(self,appointment_id):
        """ Delete a specific appointment """
        pass

class AppointmentsActionsClose(Resource):
    def post(self,appointment_id):
        """ Close a open appointment """
        pass

class AppointmentsActionsReschedule(Resource):
    def post(self,appointment_id):
        """ Reschedule a specific appointment to a new date """
        pass
