from zione.core.enums import Status
from zione.core.exceptions import MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.entities.user import User
from zione.domain.usecases.add_user import add_user_usecase


class TestAddUserUsecase:
    user_dict = {
        "id": 2,
        "username": "lucca",
        "password": "cocomelon"
    }

    user = User(
        id = 2,
        username = "lucca",
        password = "cocomelon"
    )

    def test_usecase_return_response_instance(self, repo_stub):
        res = add_user_usecase(repo_stub, self.user_dict)

        assert isinstance(res, Response)

    def test_dict_with_missings_fields_should_return_http_code_406(self, repo_stub):
        user_dict = self.user_dict
        if user_dict.get("password"):
            self.user_dict.pop("password")
        res = add_user_usecase(repo_stub, self.user_dict)

        assert res.http_code == 406

    def test_dict_with_missings_fields_should_return_error(self, repo_stub):
        user_dict = self.user_dict
        if user_dict.get("password"):
            self.user_dict.pop("password")
        res = add_user_usecase(repo_stub, self.user_dict)

        assert res.error == MissingFieldError()

    def test_dict_with_missings_fields_should_return_message(self, repo_stub):
        user_dict = self.user_dict
        if user_dict.get("password"):
            self.user_dict.pop("password")
        res = add_user_usecase(repo_stub, self.user_dict)

        assert "missing 1 required positional argument" in res.message

    def test_dict_with_missings_fields_should_return_status_error(self, repo_stub):
        user_dict = self.user_dict
        if user_dict.get("password"):
            self.user_dict.pop("password")
        res = add_user_usecase(repo_stub, self.user_dict)

        assert res.status == Status.Error

    def test_valid_dict_should_return_http_cod_200(self, repo_stub):
        user_dict = self.user.to_dict()
        if user_dict.get("id"):
            self.user_dict.pop("id")
        res = add_user_usecase(repo_stub, user_dict)

        assert res.http_code == 200
