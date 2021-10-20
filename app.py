from flask import Flask
from flask_restful import Resource, Api
from api.tickets.view import TicketOpen, Tickets, TicketsActionsClose
from api.appointments.view import Appointments, AppointmentOpen, AppointmentsActionsClose, AppointmentsActionsReschedule
# from api.tickets.view import TicketOpen, Tickets, TicketsActionsClose
# from api.appointments.view import Appointments, AppointmentsActionsClose, AppointmentsActionsReschedule

# from db import db

app = Flask(__name__)
api = Api(app)

api.add_resource(TicketOpen, "/tickets")
api.add_resource(Tickets, "/tickets/<string:id>")
api.add_resource(TicketsActionsClose, "/tickets/<string:id>/actions/close")
api.add_resource(AppointmentOpen, "/appointments")
api.add_resource(Appointments, "/appointments/<string:appointment_id>")
api.add_resource(AppointmentsActionsClose, "/appointments/<string:appointment_id>/actions/close")
api.add_resource(AppointmentsActionsReschedule, "/appointments/<string:appointment_id>/actions/reschedule")

if __name__ == '__main__':
    # db.init_app(app)
    app.run()
