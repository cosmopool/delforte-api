import pytest
from webtest import TestApp
from tests.stubs.repository_stub import RepositoryStub

from zione.app import create_app
from zione.core.dependency_injection import make_repository
from zione.core.settings import TestConfig
from zione.infra.repositories.postgres_repository import PostgresRepository

@pytest.yield_fixture(scope='function')
def app():
    """An application for running tests"""
    _app = create_app(TestConfig)

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

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
