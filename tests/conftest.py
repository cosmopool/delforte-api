import pytest
from webtest import TestApp
from tests.stubs.repository_stub import RepositoryStub

from zione.app import create_app
from zione.core.dependency_injection import make_repository
from zione.core.settings import TestConfig
from zione.infra.repositories.postgres_repository import PostgresRepository

@pytest.fixture(scope='function')
def app():
    """An application for running tests"""
    _app = create_app(TestConfig)

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture(scope='function')
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""

    return TestApp(app)

@pytest.fixture(scope='function')
def repo(app):
    """A repository with connection to real database."""

    return make_repository(app, PostgresRepository)

@pytest.fixture(scope='function')
def repo_stub(app):
    """A repository with connection to real database."""

    return make_repository(app, RepositoryStub)

@pytest.fixture(scope='function')
def ap():
    """A repository with connection to real database."""

    return {
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "isFinished": False,
    }

@pytest.fixture(scope='function')
def tk():
    """A repository with connection to real database."""

    return {
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False,
    }

@pytest.fixture(scope='function')
def ag():
    """A repository with connection to real database."""

    return {
        "time": "15:00",
        "date": "12-16-2021",
        "duration": "1:30",
        "clientName": "Roberta Baroa",
        "clientAddress": "Rua David Campista, 666",
        "clientPhone": 41777222000,
        "serviceType": "Orcamento",
        "description": "Cameras e alarme",
    }

@pytest.fixture(scope='function')
def user():
    """Return a valid user for authentication"""
    
    return {"username": "kaio", "password": "kaio123"}

@pytest.fixture()
def token(client, user):
    """Return token to be used in requests headers"""

    res = client.post(f"login", json=user)
    return res.json['Result'][0]

@pytest.fixture()
def headers(token):
    """Return header with authorization token to be used in tests"""

    return {'Content-Type': 'application/json', "Authorization": f"Bearer {token}"}

@pytest.fixture()
def add_ap(client, headers, ap) -> int:
    """Return the last entry from open tickets"""
    
    res = client.post("appointments", headers=headers, json=ap)
    appointment_id = res.json['Result'][0]

    return appointment_id

@pytest.fixture()
def add_tk(client, headers, tk) -> int:
    """Return the last entry from open tickets"""
    
    res = client.post("tickets", headers=headers, json=tk)
    ticket_id = res.json['Result'][0]

    return ticket_id

@pytest.fixture()
def last_tk(client, headers) -> tuple[dict, str]:
    """Return the last entry from open tickets"""
    
    res = client.get("tickets", headers=headers)
    result = res.json['Result']

    last_index = len(result) - 1
    last_item = result[last_index]
    endpoint = f"tickets/{last_item['id']}"
    return last_item, endpoint
