import json
import logging
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_appointment import add_appointment_usecase
from zione.domain.usecases.close_appointment import close_appointment_usecase
from zione.domain.usecases.delete_appointment import delete_appointment_usecase
from zione.domain.usecases.edit_appointment import edit_appointment_usecase
from zione.domain.usecases.fetch_appointment import fetch_appointment_usecase
from zione.domain.usecases.fetch_open_appointments import fetch_open_appointments_usecase
from zione.domain.usecases.reschedule_appointment import reschedule_appointment_usecase
from zione.interface.utils.response import cook_response


class AppointmentOpen(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def get(self):
        """Get all open appointments"""
        logging.info("[ENDPOINT][APPOINTMENT] GET request at: /appointments... calling use case")

        response = fetch_open_appointments_usecase(self._repository)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from fetch open appointments use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def post(self):
        """Book a new appointment"""
        logging.info("[ENDPOINT][APPOINTMENT] POST request at: /appointments... calling use case")

        entry = json.loads(request.data)
        response = add_appointment_usecase(self._repository, entry)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from add appointment use case: {response}")

        return cook_response(raw_response=response)


class Appointments(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def get(self, id):
        """Get information about specific appointment"""
        logging.info("[ENDPOINT][APPOINTMENT] GET request at: /appointments... calling use case")

        response = fetch_appointment_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from fetch appointment use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def patch(self, id):
        """Edit a specific appointment"""
        entry = json.loads(request.data)
        logging.info("[ENDPOINT][APPOINTMENT] PATCH request at: /appointments... calling use case")

        response = edit_appointment_usecase(self._repository, entry, id)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from edit appointment use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def delete(self, id):
        """Delete a specific appointment"""
        logging.info("[ENDPOINT][APPOINTMENT] DELETE request at: /appointments... calling use case")

        response = delete_appointment_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from delete appointment use case: {response}")

        return cook_response(raw_response=response)


class AppointmentsActionsClose(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def post(self, id):
        """Close a open appointment"""
        logging.info("[ENDPOINT][APPOINTMENT] POST request at: /appointments... calling use case")

        response = close_appointment_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from close appointment use case: {response}")

        return cook_response(raw_response=response)


class AppointmentsActionsReschedule(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def post(self, id):
        """Reschedule a specific appointment to a new date"""
        entry = json.loads(request.data)
        logging.info("[ENDPOINT][APPOINTMENT] POST request at: /appointments... calling use case")

        response = reschedule_appointment_usecase(self._repository, entry, id)
        logging.debug(f"[ENDPOINT][APPOINTMENT] response from reschedule appointment use case: {response}")

        return cook_response(raw_response=response)
