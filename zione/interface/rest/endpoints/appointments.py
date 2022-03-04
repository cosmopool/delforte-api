import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_appointment import add_appointment_usecase
from zione.domain.usecases.close_appointment import close_appointment_usecase
from zione.domain.usecases.edit_appointment import edit_appointment_usecase
from zione.domain.usecases.fetch_appointment import fetch_appointment_usecase
from zione.domain.usecases.fetch_open_appointments import fetch_open_appointments_usecase
from zione.domain.usecases.reschedule_appointment import reschedule_appointment_usecase


@dataclass
class AppointmentOpen(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self):
        """get all open appointments"""
        response = fetch_open_appointments_usecase(self._repository)
        logging.debug(f"Response from usecase: {response}")
        logging.debug(f"GET request at: /appointments/")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


    @jwt_required()
    def post(self):
        """Book a new appointment"""
        entry = json.loads(request.data)
        logging.debug(f"POST request at: /appointments/")
        logging.debug(f"Request data: {request.data}")

        response = add_appointment_usecase(self._repository, entry)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


@dataclass
class Appointments(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self, id):
        """Get information about specific appointment"""
        logging.debug(f"GET request at: /appointments/id")
        logging.debug(f"Request parameter: {id}")

        response = fetch_appointment_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


    @jwt_required()
    def patch(self, id):
        """Edit a specific appointment"""
        entry = json.loads(request.data)
        logging.debug(f"PATCH request at: /appointments/id")
        logging.debug(f"Request parameter: {id}")
        logging.debug(f"Request data: {request.data}")

        response = edit_appointment_usecase(self._repository, entry)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


    @jwt_required()
    def delete(self, id):
        """Delete a specific appointment"""
        logging.debug(f"DELETE request at: /appointments/id")
        logging.debug(f"Request parameter: {id}")

        response = edit_appointment_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


@dataclass
class AppointmentsActionsClose(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def post(self, id):
        """Close a open appointment"""
        logging.debug(f"POST request at: /appointments/id/actions/close")
        logging.debug(f"Request parameter: {id}")

        response = close_appointment_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


@dataclass
class AppointmentsActionsReschedule(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def post(self, id):
        """Reschedule a specific appointment to a new date"""
        entry = json.loads(request.data)
        logging.debug(f"PATCH request at: /appointments/id/actions/reschedule")
        logging.debug(f"Request parameter: {id}")
        logging.debug(f"Request data: {request.data}")

        response = reschedule_appointment_usecase(self._repository, entry, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code
