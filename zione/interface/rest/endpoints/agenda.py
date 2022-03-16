import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from zione.domain.repository_interface import RepositoryInterface
from zione.domain.usecases.add_agenda_entry import add_agenda_entry_usecase
from zione.domain.usecases.fetch_agenda import fetch_agenda_usecase
from zione.interface.utils.response import cook_response


@dataclass
class Agenda(Resource):
    _repository: RepositoryInterface

    @jwt_required()
    def get(self):
        logging.info("[ENDPOINT][AGENDA] get request at: /agenda")

        response = fetch_agenda_usecase(self._repository)
        logging.debug(f"[ENDPOINT][AGENDA] response from fetch_agenda_usecase: {response}")

        return cook_response(raw_response=response)

    def post(self):
        logging.info("[ENDPOINT][AGENDA] post request at: /agenda")
        logging.debug(f"[ENDPOINT][AGENDA] request data: {request.data}")

        entry = json.loads(request.data)
        response = add_agenda_entry_usecase(self._repository, entry)
        logging.debug(f"[ENDPOINT][AGENDA] response from add_agenda_usecase: {response}")

        return cook_response(raw_response=response)
