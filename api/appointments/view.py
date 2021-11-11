from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from db import insert, select, delete, update
from .model import AppointmentSchema

class AppointmentOpen(Resource):
    @jwt_required()
    def get(self):
        """ get all open appointments """
        try:
            result = select("appointments", {"id": "> 0"})
        except Exception as e:
            message = "Error"
            result = ["Something went wrong while searching your data", e]
            http_status = 500
        else:
            message = "Open Appointments"
            http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

    @jwt_required()
    def post(self):
        """ Book a new appointment """
        schema = AppointmentSchema()
        try:
            appointment = schema.load(request.json)
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 406
        else:
            try:
                result = insert("appointments", appointment)
            except Exception as e:
                message = "Error"
                result = ["Something went wrong while searching your data", e]
                http_status = 500
            else:
                message = "Appointment booked"
                http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

class Appointments(Resource):
    @jwt_required()
    def get(self, appointment_id):
        """ Get information about specific appointment """
        try:
            result = select("appointments", {"id": appointment_id})
        except Exception as e:
            message = "Error"
            result = ["Something went wrong while searching your data", e]
            http_status = 500
        else:
            message = "Appointment"
            http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

    @jwt_required()
    def patch(self,appointment_id):
        """ Edit a specific appointment """
        schema = AppointmentSchema(partial=True)
        ticket = schema.load(request.json)
        try:
            appointment = self.__val_appointment__(appointment, id)
        except ValueError:
            message = "Error"
            result = "Id do not match"
            http_status = 406
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 406
        else:
            try:
                result = update("appointments", {"id": id}, appointment)
            except Exception as e:
                message = "Error"
                result = ["Value too long", e]
                http_status = 409
            else:
                message = "Message"
                if result == 0:
                    http_status = 406
                else:
                    http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

    def __val_appointment__(self, ticket, id):
        # validade ticket id and id
        if str(ticket.get("id")) == str(id):
            return ticket
        else:
            raise ValueError("Id do not match.")

        if ticket.get("is_finished"):
            ticket.pop("is_finished")
        if ticket.get("id"):
            ticket.pop("id")

    @jwt_required()
    def delete(self,appointment_id):
        """ Delete a specific appointment """
        pass

class AppointmentsActionsClose(Resource):
    @jwt_required()
    def post(self,appointment_id):
        """ Close a open appointment """
        try:
            result = update("appointments", {"id": appointment_id}, {"is_finished": "true"})
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 500
        else:
            message = "Success"
            http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status

class AppointmentsActionsReschedule(Resource):
    @jwt_required()
    def post(self, appointment_id):
        """ Reschedule a specific appointment to a new date """
        # print(f"------------------------------ {request.json}")
        schema = AppointmentSchema(partial=True)
        try:
            appointment = schema.load(request.json)
        except Exception as e:
            message = "Error"
            result = str(e)
            http_status = 406
        else:
            try:
                result = update("appointments", {"id": appointment_id}, appointment)
                print(f"--------------------------- { appointment }")
            except Exception as e:
                message = "Error"
                # result = "Something went wrong"
                result = str(e)
                http_status = 500
            else:
                message = "Success"
                http_status = 200
        finally:
            return {"Status": message, "Result": result}, http_status
