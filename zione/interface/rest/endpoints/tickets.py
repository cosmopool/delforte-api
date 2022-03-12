import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_ticket import add_ticket_usecase
from zione.domain.usecases.close_ticket import close_ticket_usecase
from zione.domain.usecases.edit_ticket import edit_ticket_usecase
from zione.domain.usecases.fetch_open_tickets import fetch_open_tickets_usecase
from zione.domain.usecases.fetch_ticket import fetch_ticket_usecase


@dataclass
class TicketOpen(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self):
        """Get all open tickets"""
        response = fetch_open_tickets_usecase(self._repository)
        logging.debug(f"Response from usecase: {response}")
        logging.debug("GET request at: /tickets/")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code

    @jwt_required()
    def post(self):
        """Open a new ticket"""
        entry = json.loads(request.data)
        logging.debug("POST request at: /tickets/")
        logging.debug(f"Request data: {request.data}")

        response = add_ticket_usecase(self._repository, entry)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


@dataclass
class Tickets(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self, id):
        """Get information about specific ticket"""
        logging.debug("GET request at: /tickets/id")
        logging.debug(f"Request parameter: {id}")

        response = fetch_ticket_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code

    @jwt_required()
    def patch(self, id):
        """Edit a specific ticket"""
        entry = json.loads(request.data)
        logging.debug("PATCH request at: /tickets/id")
        logging.debug(f"Request parameter: {id}")
        logging.debug(f"Request data: {request.data}")

        response = edit_ticket_usecase(self._repository, entry)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code

    # @jwt_required()
    def delete(self, id):
        """Delete a specific ticket"""
        logging.debug("DELETE request at: /tickets/id")
        logging.debug(f"Request parameter: {id}")

        response = edit_ticket_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code


@dataclass
class TicketsActionsClose(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def post(self, id):
        """Close a open ticket"""
        logging.debug("POST request at: /tickets/id/actions/close")
        logging.debug(f"Request parameter: {id}")

        response = close_ticket_usecase(self._repository, id)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code
