from flask_restful import Resource, reqparse

class TicketOpen(Resource):
    def post(self):
        """ Open a new ticket """
        pass

class Tickets(Resource):
    def get(self, id):
        """ Get information about specific ticket """
        pass

    def patch(self, id):
        """ Edit a specific ticket """
        pass

    def delete(self, id):
        """ Delete a specific ticket """
        pass

class TicketsActionsClose(Resource):
    def post(self, id):
        """ Close a open ticket """
        pass
