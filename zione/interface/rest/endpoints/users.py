import json
import logging
from flask import request
from flask_restx import Resource
from flask_jwt_extended import create_access_token
from zione.core.enums import Status

from zione.domain.usecases.authenticate_user import authenticate_user_usecase
from zione.domain.repository_interface import RepositoryInterface


# @dataclass
class UserAuthenticate(Resource):
    _repository: RepositoryInterface

    def __init__(self, *args, **kwargs):
        self._repository = kwargs['_repository']

    def post(self):
        """Authenticate a user given a username and password"""
        entry = json.loads(request.data)
        logging.info("[USER] post request at: /login")
        logging.debug(f"Request data: {request.data}")

        response = authenticate_user_usecase(self._repository, entry, create_access_token)
        result = response.result if response.status == Status.Success else response.message
        logging.debug(f"Response from usecase: {response}")

        return {
            "Status": f"{response.status}",
            "Result": result,
        }, response.http_code
