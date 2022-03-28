import logging

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow.fields import String

from zione.core.dependency_injection import make_repository
from zione.core.settings import ProdConfig
from zione.interface.rest.endpoints.agenda import Agenda
from zione.interface.rest.endpoints.appointments import AppointmentOpen, Appointments, AppointmentsActionsClose, AppointmentsActionsReschedule
from zione.interface.rest.endpoints.tickets import TicketOpen, Tickets, TicketsActionsClose
from zione.interface.rest.endpoints.users import UserAuthenticate


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    logging.basicConfig(level=config_object.LOG_LEVEL)
    app.config.from_object(config_object)
    jwt = JWTManager(app)
    repo = {"_repository": make_repository(app)}

    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def my_unauthorized_loader(err: String):
        return {"Status": "Error", "Result": f"Authentication token error: {err}"}, 401

    @jwt.needs_fresh_token_loader
    @jwt.revoked_token_loader
    @jwt.expired_token_loader
    @jwt.token_verification_failed_loader
    def my_expired_token_callback(jwt_header: dict, jwt_payload: dict):
        return {"Status": "Error", "Result": f"Authentication token error. {jwt_header}. {jwt_payload}"}, 401

    register_agenda_endpoints(app, repo)
    register_tickets_endpoints(app, repo)
    register_appointments_endpoints(app, repo)
    register_users_endpoints(app, repo)

    return app


def register_agenda_endpoints(app: Flask, repo: dict):
    """Register all agenda endpoints"""
    api = Api(app)
    api.add_resource(Agenda, "/agenda", resource_class_kwargs=repo)


def register_tickets_endpoints(app: Flask, repo: dict):
    """Register all tickets endpoints"""
    api = Api(app)
    api.add_resource(TicketOpen, "/tickets", resource_class_kwargs=repo)
    api.add_resource(Tickets, "/tickets/<string:id>", resource_class_kwargs=repo)
    api.add_resource(
        TicketsActionsClose,
        "/tickets/<string:id>/actions/close",
        resource_class_kwargs=repo,
    )


def register_appointments_endpoints(app: Flask, repo: dict):
    """Register all appointments endpoints"""
    api = Api(app)
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


def register_users_endpoints(app: Flask, repo: dict):
    """Register all users endpoints"""
    api = Api(app)
    api.add_resource(UserAuthenticate, "/login", resource_class_kwargs=repo)
