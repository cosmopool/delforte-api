from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required


from .model import AppointmentSchema
from zione.db import insert, select, delete, update
from zione.response.view import handle_request, handle_request_with_schema

class AppointmentOpen(Resource):
    @jwt_required()
    def get(self):
        """ get all open appointments """
        query_type = select
        table = "appointments"
        val = {"id": "> 0"}
        msg_ok = "Open Appointments"

        return handle_request(query_type, table, val, msg_ok)

    @jwt_required()
    def post(self):
        """ Book a new appointment """
        query_type = insert
        table = "appointments"
        schema = AppointmentSchema
        msg_ok = "Appointment Booked"

<<<<<<< HEAD
        return handle_request_with_schema(query_type, table, schema, msg_ok)

class Appointments(Resource):
    @jwt_required()
    def get(self, appointment_id):
        """ Get information about specific appointment """
        query_type = select
        table = "appointments"
        val = {"id": appointment_id}
=======
        return handle_request_with_schema(request.json, request.json, query_type, table, schema, msg_ok)

class Appointments(Resource):
    @jwt_required()
    def get(self, appointmentId):
        """ Get information about specific appointment """
        query_type = select
        table = "appointments"
        val = {"id": appointmentId}
>>>>>>> feature/address-geocoding

        return handle_request(query_type, table, val)

    @jwt_required()
<<<<<<< HEAD
    def patch(self,appointment_id):
=======
    def patch(self,appointmentId):
>>>>>>> feature/address-geocoding
        """ Edit a specific appointment """
        query_type = update
        table = "appointments"
        schema = AppointmentSchema
        schema_partial = True
<<<<<<< HEAD
        # query_vals = {"id": appointment_id}
        query_vals = appointment_id
        err_code = 409

        return handle_request_with_schema(query_type, table, schema, schema_partial, msg_ok, query_vals=query_vals, err_code=err_code)
=======
        # query_vals = {"id": appointmentId}
        query_vals = appointmentId
        err_code = 409

        return handle_request_with_schema(request.json, query_type, table, schema, schema_partial, msg_ok, query_vals=query_vals, err_code=err_code)
>>>>>>> feature/address-geocoding

    def __val_appointment__(self, dict, id):
        # validade ticket id and id
        # n_dict = dict
        # if str(dict.get("id")) == str(id):
        #     return dict
        # else:
        #     raise ValueError("Id do not match.")

        # if dict.get("is_finished"):
        #     dict.pop("is_finished")
        # if dict.get("id"):
        #     dict.pop("id")

        # return dict
        pass

    @jwt_required()
<<<<<<< HEAD
    def delete(self,appointment_id):
        """ Delete a specific appointment """
        pass

class AppointmentsActionsClose(Resource):
    @jwt_required()
    def post(self,appointment_id):
        """ Close a open appointment """
        query_type = update
        table = "appointments"
        val = {"id": appointment_id}
=======
    def delete(self,appointmentId):
        """ Delete a specific appointment """
        query_type = delete
        table = "appointments"
        val = {"id": appointmentId}

        return handle_request(query_type, table, val)

class AppointmentsActionsClose(Resource):
    @jwt_required()
    def post(self,appointmentId):
        """ Close a open appointment """
        query_type = update
        table = "appointments"
        val = {"id": appointmentId}
>>>>>>> feature/address-geocoding

        return handle_request(query_type, table, val)

class AppointmentsActionsReschedule(Resource):
    @jwt_required()
<<<<<<< HEAD
    def post(self, appointment_id):
        """ Reschedule a specific appointment to a new date """
=======
    def post(self, appointmentId):
        """ Reschedule a specific appointment to a new date """
        # TODO: need to test to see if it is working
>>>>>>> feature/address-geocoding
        query_type = update
        table = "appointments"
        schema = AppointmentSchema
        schema_partial = True
<<<<<<< HEAD
        # query_vals = {"id": appointment_id}
        query_vals = appointment_id

        # return handle_request_with_schema(update, table, schema, schema_partial, query_vals=query_vals, err_code=err_code)
        return handle_request_with_schema(query_type, table, schema, schema_partial, query_vals=query_vals)
=======
        # query_vals = {"id": appointmentId}
        query_vals = appointmentId

        # return handle_request_with_schema(request.json, update, table, schema, schema_partial, query_vals=query_vals, err_code=err_code)
        return handle_request_with_schema(request.json, query_type, table, schema, schema_partial, query_vals=query_vals)
>>>>>>> feature/address-geocoding
