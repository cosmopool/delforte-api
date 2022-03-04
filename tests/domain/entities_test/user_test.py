import pytest
from zione.domain.entities.user import User


class TestUserInstance:
    user_dict = {"id": 1, "username": "gladson", "password": "123456"}

    def test_userpointment_entity_init(self):
        user = User(id = 1, username = "gladson", password = "123456")

        assert user.id == 1
        assert user.username == "gladson"
        assert user.password == "123456"

    def test_userpointment_entity_to_dict(self):
        user = User(id = 1, username = "gladson", password = "123456")
        
        assert user.to_dict() == self.user_dict

    def test_userpointment_entity_from_dict(self):
        user = User.from_dict(self.user_dict)
        
        assert user.id == 1
        assert user.username == "gladson"
        assert user.password == "123456"

    def test_userpointment_entity_comparison(self):
        user1 = User(id = 1, username = "gladson", password = "123456")
        user2 = User.from_dict(self.user_dict)

        assert user1 == user2

    def test_user_entity_to_dict_with_additional_fields(self):
        additonal_field = {
        "id": 1,
        "username": "gladson",
        "password": "123456",
        "duration": "1:00",
        "userId": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
        }
        user = User.from_dict(additonal_field)

        assert user.to_dict() == self.user_dict

    def test_user_entity_to_dict_with_missing_fields(self):
        missing_field = {"id": 1, "username": "gladson"}

        with pytest.raises(TypeError):
            _ = User.from_dict(missing_field)

    def test_user_entity_from_dict_default_id_value(self):
        usr_dict = {"password": "123456", "username": "gladson"}
        user = User.from_dict(usr_dict)

        assert user.id == -1

    def test_user_entity_endpoint_value(self):
        endpoint = User.endpoint

        assert endpoint == "users"
