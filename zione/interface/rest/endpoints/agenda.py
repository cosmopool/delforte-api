import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.fetch_agenda import fetch_agenda_usecase
from zione.domain.usecases.add_ticket import add_ticket_usecase
from zione.domain.usecases.add_appointment import add_appointment_usecase


@dataclass
class Agenda(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self):
        logging.debug("GET request at: /agenda")
        response = fetch_agenda_usecase(self._repository)
        logging.debug(f"Response from usecase: {response}")
        print(response)

        return {"Status": f"{response.status}", "Result": response.result}, response.http_code

    def post(self):
        logging.debug("POST request at: /agenda")
        logging.debug(f"Request data: {request.data}")
        # TODO: add a use case for add and agenda entry
        # TODO: add a use case for add and agenda entry
        # TODO: add a use case for add and agenda entry
        entry = json.loads(request.data)
        response_ap = add_appointment_usecase(self._repository, entry)
        response_tk = add_ticket_usecase(self._repository, entry)
        ap_code = response_ap.http_code
        tk_code = response_tk.http_code

        if ap_code == 200 and tk_code == 200:
            return {"Status": "Success", "Result": "Agenda entry saved with success"}, 200
        elif ap_code != 200 and tk_code == 200:
            return {"Status": "Error", "Result": "Appointment was add with success, but ticket didn't"}, 200
        elif ap_code == 200 and tk_code != 200:
            return {"Status": "Error", "Result": "Ticket was add with success, but appointment didn't"}, 200
        else:
            return {"Status": "Error", "Result": "Could not add none of the entries"}, 200
