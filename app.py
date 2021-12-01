import os

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from zione import db
from zione.users.view import User, Users, UserAuthenticate
from zione.tickets.view import TicketOpen, Tickets, TicketsActionsClose
from zione.appointments.view import Appointments, AppointmentOpen, AppointmentsActionsClose, AppointmentsActionsReschedule
from zione.agenda.view import Agenda

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = os.environ.get("SECRET")

jwt = JWTManager(app)

api.add_resource(Agenda, "/agenda")

api.add_resource(TicketOpen, "/tickets")
api.add_resource(Tickets, "/tickets/<string:ticket_id>")
api.add_resource(TicketsActionsClose, "/tickets/<string:ticket_id>/actions/close")

api.add_resource(AppointmentOpen, "/appointments")
api.add_resource(Appointments, "/appointments/<string:appointment_id>")
api.add_resource(AppointmentsActionsClose, "/appointments/<string:appointment_id>/actions/close")
api.add_resource(AppointmentsActionsReschedule, "/appointments/<string:appointment_id>/actions/reschedule")

api.add_resource(User, "/users")
api.add_resource(Users, "/users/<string:user_id>")
api.add_resource(UserAuthenticate, "/login")
