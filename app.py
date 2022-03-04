import os
import logging

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from zione.core.dependency_injection import REPOSITORY
from zione.interface.rest.endpoints.agenda import Agenda
from zione.interface.rest.endpoints.appointments import AppointmentOpen, Appointments, AppointmentsActionsClose, AppointmentsActionsReschedule
from zione.interface.rest.endpoints.tickets import TicketOpen, Tickets, TicketsActionsClose
from zione.interface.rest.endpoints.users import UserAuthenticate

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = os.environ.get("SECRET")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)
repo = {"_repository": REPOSITORY}

api.add_resource(Agenda, "/agenda", resource_class_kwargs=repo)

api.add_resource(TicketOpen, "/tickets", resource_class_kwargs=repo)
api.add_resource(Tickets, "/tickets/<string:id>", resource_class_kwargs=repo)
api.add_resource(TicketsActionsClose, "/tickets/<string:id>/actions/close", resource_class_kwargs=repo)

api.add_resource(AppointmentOpen, "/appointments", resource_class_kwargs=repo)
api.add_resource(Appointments, "/appointments/<string:id>", resource_class_kwargs=repo)
api.add_resource(AppointmentsActionsClose, "/appointments/<string:id>/actions/close", resource_class_kwargs=repo)
api.add_resource(AppointmentsActionsReschedule, "/appointments/<string:id>/actions/reschedule", resource_class_kwargs=repo)

api.add_resource(UserAuthenticate, "/login", resource_class_kwargs=repo)
