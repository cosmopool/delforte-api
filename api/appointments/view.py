from flask_restful import Resource

class Appointments(Resource):
    def post(self, ticket_id):
        """ Book a new appointment """
        pass

    def get(self,appointment_id):
        """ Get information about specific appointment """
        pass

    def patch(self,appointment_id):
        """ Edit a specific appointment """
        pass

    def delete(self,appointment_id):
        """ Delete a specific appointment """
        pass

class AppointmentsActionsClose(Resource):
    def post(self,appointment_id):
        """ Close a open appointment """
        pass

class AppointmentsActionsReschedule(Resource):
    def post(self,appointment_id):
        """ Reschedule a specific appointment to a new date """
        pass
