import json
import logging
from flask import request
from dataclasses import dataclass
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from zione.domain.usecases.authenticate_user import authenticate_user_usecase
from zione.domain.repository_interface import RepositoryInterface


@dataclass
class UserAuthenticate(Resource):
    _repository: RepositoryInterface

    def post(self):
        """Authenticate a user given a username and password"""
        entry = json.loads(request.data)
        logging.debug("POST request at: /login")
        logging.debug(f"Request data: {request.data}")

        response = authenticate_user_usecase(self._repository, entry, create_access_token)
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": response.result,
        }, response.http_code
