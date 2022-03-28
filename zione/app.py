import logging

from flask import Flask
from flask_restx import Api
from flask_jwt_extended.jwt_manager import JWTManager
from flask_jwt_extended.exceptions import JWTExtendedException
from jwt.exceptions import PyJWTError
from marshmallow.fields import String
from zione.core.dependency_injection import make_repository

from zione.core.settings import ProdConfig
from zione.domain.repository_interface import RepositoryInterface
from zione.infra.repositories.postgres_repository import PostgresRepository
from zione.interface.rest import endpoints
from zione.interface.rest.endpoints.agenda import Agenda
from zione.interface.rest.endpoints.appointments import (
    AppointmentOpen,
    Appointments,
    AppointmentsActionsClose,
    AppointmentsActionsReschedule,
)
from zione.interface.rest.endpoints.tickets import (
    TicketOpen,
    Tickets,
    TicketsActionsClose,
)
from zione.interface.rest.endpoints.users import UserAuthenticate


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    logging.basicConfig(level=config_object.LOG_LEVEL)
    app.config.from_object(config_object)

    repo = {"_repository": PostgresRepository(app.config["CONNECTION"])}
    # repo = [make_repository(app)]

    _ = JWTManager(app)
    api = Api(app)

    @api.errorhandler(JWTExtendedException)
    @api.errorhandler(PyJWTError)
    def handle_jwt_exceptions(err: String):
        return {"Status": "Error", "Result": f"Authentication token error: {err}"}, 401

    register_agenda_endpoints(api, repo)
    register_tickets_endpoints(api, repo)
    register_appointments_endpoints(api, repo)
    register_users_endpoints(api, repo)

    api.init_app(app, add_specs=False)
    return app


def register_agenda_endpoints(api: Api, repo: dict):
    """Register all agenda endpoints"""
    api.add_resource(Agenda, "/agenda", resource_class_kwargs=repo)
    # api.add_resource(Agenda, "/agenda", {"_repository": make_repository(app)})


def register_tickets_endpoints(api: Api, repo: dict):
    """Register all tickets endpoints"""
    api.add_resource(TicketOpen, "/tickets", resource_class_kwargs=repo)
    api.add_resource(Tickets, "/tickets/<string:id>", resource_class_kwargs=repo)
    api.add_resource(
        TicketsActionsClose,
        "/tickets/<string:id>/actions/close",
        resource_class_kwargs=repo,
    )


def register_appointments_endpoints(api: Api, repo: dict):
    """Register all appointments endpoints"""
    api.add_resource(AppointmentOpen, "/appointments", resource_class_kwargs=repo)
    api.add_resource(
        Appointments, "/appointments/<string:id>", resource_class_kwargs=repo
    )
    api.add_resource(
        AppointmentsActionsClose,
        "/appointments/<string:id>/actions/close",
        resource_class_kwargs=repo,
    )
    api.add_resource(
        AppointmentsActionsReschedule,
        "/appointments/<string:id>/actions/reschedule",
        resource_class_kwargs=repo,
    )


def register_users_endpoints(api: Api, repo: dict):
    """Register all users endpoints"""
    api.add_resource(UserAuthenticate, "/login", resource_class_kwargs=repo)
