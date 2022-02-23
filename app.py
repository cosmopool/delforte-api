import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from zione.users.view import User, Users, UserAuthenticate
from zione.tickets.view import TicketOpen, Tickets, TicketsActionsClose
from zione.appointments.view import Appointments, AppointmentOpen, AppointmentsActionsClose, AppointmentsActionsReschedule
from zione.agenda.view import Agenda

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = os.environ.get("SECRET")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)

api.add_resource(Agenda, "/agenda")

api.add_resource(TicketOpen, "/tickets")
api.add_resource(Tickets, "/tickets/<string:ticketId>")
api.add_resource(TicketsActionsClose, "/tickets/<string:ticketId>/actions/close")

api.add_resource(AppointmentOpen, "/appointments")
api.add_resource(Appointments, "/appointments/<string:appointmentId>")
api.add_resource(AppointmentsActionsClose, "/appointments/<string:appointmentId>/actions/close")
api.add_resource(AppointmentsActionsReschedule, "/appointments/<string:appointmentId>/actions/reschedule")

api.add_resource(User, "/users")
api.add_resource(Users, "/users/<string:user_id>")
api.add_resource(UserAuthenticate, "/login")
