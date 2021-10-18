from flask import Flask
from flask_restful import Resource, Api

from db import db

app = Flask(__name__)
api = Api(app)

api.add_resource(TicketOpen, "/tickets")
api.add_resource(Tickets, "/tickets/<string:id>")
api.add_resource(TicketsActionsClose, "/tickets/<string:id>/actions/close")
api.add_resource(Appointments, "/appointments/<string:id>")
api.add_resource(AppointmentsActionsClose, "/appointments/<string:id>/actions/close")
api.add_resource(AppointmentsActionsReschedule, "/appointments/<string:id>/actions/reschedule")

if __name__ == '__main__':
    db.init_app(app)
    app.run()
