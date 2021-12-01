from flask_restful import Resource
from flask_jwt_extended import jwt_required

from .model import TicketSchema
from zione.db import insert, select, delete, update
from zione.response.view import handle_request, handle_request_with_schema

class TicketOpen(Resource):
    @jwt_required()
    def get(self):
        """ Get all open tickets """
        query_type = select
        table = "tickets"
        val = {"is_finished": "= false"}

        return handle_request(query_type, table, val)



    @jwt_required()
    def post(self):
        """ Open a new ticket """
        query_type = insert
        table = "tickets"
        schema = TicketSchema
        msg_ok = "Ticket Opened"

        return handle_request_with_schema(query_type, table, schema, msg_ok)



class Tickets(Resource):
    @jwt_required()
    def get(self, ticket_id):
        """ Get information about specific ticket """
        query_type = select
        table = "appointments"
        val = {"id": ticket_id}

        return handle_request(query_type, table, val)



    @jwt_required()
    def patch(self, ticket_id):
        """ Edit a specific ticket """
        query_type = update
        table = "tickets"
        schema = TicketSchema
        schema_partial = True
        query_vals = ticket_id

        return handle_request_with_schema(query_type, table, schema, schema_partial, query_vals=query_vals)



    @jwt_required()
    def delete(self, ticket_id):
        """ Delete a specific ticket """
        query_type = delete
        table = "tickets"
        val = {"id": ticket_id}

        return handle_request(query_type, table, val)



    def __val_ticket__(self, ticket, id):
        # validade ticket id and id
        if str(ticket.get("id")) == str(id):
            return ticket
        else:
            raise ValueError("Id do not match.")

        if ticket.get("is_finished"):
            ticket.pop("is_finished")
        if ticket.get("id"):
            ticket.pop("id")



class TicketsActionsClose(Resource):
    @jwt_required()
    def post(self, ticket_id):
        """ Close a open ticket """
        query_type = update
        table = "ticket"
        val = {"id": ticket_id}, {"is_finished": "true"}

        return handle_request(query_type, table, val)
