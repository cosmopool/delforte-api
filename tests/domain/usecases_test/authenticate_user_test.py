from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.user import User
from zione.domain.entities.response import Response
from zione.domain.usecases.authenticate_user import authenticate_user_usecase

from tests.stubs.repository_stub import RepositoryStub

class TestAuthenticateUserUsecase:
    usr_dict = {
        # "id": 2,
        "username": "lucca",
        "password": "cocomelon"
    }

    usr = User(
        # id = 2,
        username = "lucca",
        password = "cocomelon"
    )

    repository = RepositoryStub()

    def create_token_callback_stub(self, *args, **kwargs):
        return "auth_token"

    def test_usecase_return_response_instance(self):
        res = authenticate_user_usecase(self.repository, self.usr_dict, self.create_token_callback_stub)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_http_code_406(self):
        usr_dict = self.usr_dict
        if usr_dict.get("password"):
            usr_dict.pop("password")
        res = authenticate_user_usecase(self.repository, self.usr_dict, self.create_token_callback_stub)

        assert res.http_code == 406

    def test_dict_with_missings_fields_should_return_error(self):
        usr_dict = self.usr_dict
        if usr_dict.get("password"):
            usr_dict.pop("password")
        res = authenticate_user_usecase(self.repository, self.usr_dict, self.create_token_callback_stub)

        assert res.error == MissingFieldError()

    def test_dict_with_missings_fields_should_return_message(self):
        usr_dict = self.usr_dict
        if usr_dict.get("password"):
            usr_dict.pop("password")
        res = authenticate_user_usecase(self.repository, self.usr_dict, self.create_token_callback_stub)

        assert "Missing data for required field" in res.message

    def test_dict_with_missings_fields_should_return_status_error(self):
        usr_dict = self.usr_dict
        if usr_dict.get("password"):
            usr_dict.pop("password")
        res = authenticate_user_usecase(self.repository, self.usr_dict, self.create_token_callback_stub)

        assert res.status == Status.Error

    def test_valid_dict_should_return_http_cod_200(self):
        usr_dict = self.usr.to_dict()
        if usr_dict.get("id"):
            usr_dict.pop("id")
        res = authenticate_user_usecase(self.repository, usr_dict, self.create_token_callback_stub)
        print(res)

        assert res.http_code == 200

    # def test_valid_dict_should_return_token_as_result(self):
    #     usr_dict = self.usr.to_dict()
    #     if usr_dict.get("id"):
    #         usr_dict.pop("id")
    #     res = authenticate_user_usecase(self.repository, usr_dict, self.create_token_callback_stub)
    #
    #     assert res.result == [self.create_token_callback_stub()]

    # def test_dict_with_missings_fields_should_return_http_code_406(self):
    #     pass
