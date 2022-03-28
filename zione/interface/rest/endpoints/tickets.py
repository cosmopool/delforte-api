import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_ticket import add_ticket_usecase
from zione.domain.usecases.close_ticket import close_ticket_usecase
from zione.domain.usecases.delete_ticket import delete_ticket_usecase
from zione.domain.usecases.edit_ticket import edit_ticket_usecase
from zione.domain.usecases.fetch_open_tickets import fetch_open_tickets_usecase
from zione.domain.usecases.fetch_ticket import fetch_ticket_usecase
from zione.interface.utils.response import cook_response


@dataclass
class TicketOpen(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def get(self):
        """Get all open tickets"""
        logging.info("[ENDPOINT][TICKET] GET request at: /tickets... calling use case")

        response = fetch_open_tickets_usecase(self._repository)
        logging.debug(f"[ENDPOINT][TICKET] response from fetch open tickets use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def post(self):
        """Open a new ticket"""
        logging.info("[ENDPOINT][TICKET] POST request at: /tickets... calling use case")

        entry = json.loads(request.data)
        response = add_ticket_usecase(self._repository, entry)
        logging.debug(f"[ENDPOINT][TICKET] response from add ticket use case: {response}")

        return cook_response(raw_response=response)


@dataclass
class Tickets(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def get(self, id):
        """Get information about specific ticket"""
        logging.info(f"[ENDPOINT][TICKET] GET request at: /tickets/{id}")

        response = fetch_ticket_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][TICKET] response from fetch ticket use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def patch(self, id):
        """Edit a specific ticket"""
        entry = json.loads(request.data)
        logging.info(f"[ENDPOINT][TICKET] PATCH request at: /tickets/{id}")

        response = edit_ticket_usecase(self._repository, entry, id)
        logging.debug(f"[ENDPOINT][TICKET] response from edit ticket use case: {response}")

        return cook_response(raw_response=response)

    @jwt_required()
    def delete(self, id):
        """Delete a specific ticket"""
        logging.info(f"[ENDPOINT][TICKET] DELETE request at: /tickets/{id}")

        response = delete_ticket_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][TICKET] response from delete ticket use case: {response}")

        return cook_response(raw_response=response)


@dataclass
class TicketsActionsClose(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    @jwt_required()
    def post(self, id):
        """Close a open ticket"""
        logging.info(f"[ENDPOINT][TICKET] POST request at: /tickets/{id}/actions/close")

        response = close_ticket_usecase(self._repository, id)
        logging.debug(f"[ENDPOINT][TICKET] response from close ticket use case: {response}")

        return cook_response(raw_response=response)
