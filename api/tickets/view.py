from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from db import insert, select, delete, update
from .model import TicketSchema

class TicketOpen(Resource):
    @jwt_required()
    def get(self):
        """ Get all open tickets """
        try:
            result = select("tickets", {"is_finished": "false"})
        except:
            message = "Error"
            result = "Something went wrong while searching your data"
            http_status = 500
        else:
            message = "Open Tickets"
            http_status = 200
        finally:
            return {message: result}, http_status

    @jwt_required()
    def post(self):
        """ Open a new ticket """
        schema = TicketSchema()

        try:
            result = schema.load(request.json)
        except:
            result = "some fields have invalid data"
            http_status = 406
        else:
            try:
                result = insert("tickets", result)
            except:
                message = "Error"
                result = "something went wrong writing your data"
                http_status = 500
            else:
                message = "Success"
                http_status = 200
        finally:
            return {"message": result}, http_status

class Tickets(Resource):
    @jwt_required()
    def get(self, id):
        """ Get information about specific ticket """
        schema = TicketSchema()
        try:
            result = select("tickets", {"id": id})
        except KeyError:
            message = "Error"
            result = "no record found with given id"
            http_status = 400
        except:
            message = "Error"
            result = "something went wrong while searching your data"
            http_status = 500
        else:
            message = "Message"
            result = schema.load(result[0])
            http_status = 200
        finally:
            return {message: result}, http_status

    @jwt_required()
    def patch(self, id):
        """ Edit a specific ticket """
        schema = TicketSchema(partial=True)
        ticket = schema.load(request.json)
        try:
            ticket = self.__val_ticket__(ticket, id)
        except ValueError:
            message = "Error"
            result = "id do not match"
            http_status = 406
        except ValidationError:
            message = "Error"
            result = "error validating your data"
        else:
            try:
                result = update("tickets", {"id": id}, ticket)
            except:
                message = "Error"
                result = "value too long"
                http_status = 409
            else:
                message = "Message"
                if result == 0:
                    http_status = 406
                else:
                    http_status = 200
        finally:
            return {message: result}, http_status

    @jwt_required()
    def delete(self, id):
        """ Delete a specific ticket """
        result = delete("tickets", {"id": id})

        if result == 0:
            message = "Error"
            http_status = 404
        else:
            message = "Message"
            http_status = 200

        return { message: result }, http_status

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
    def post(self, id):
        """ Close a open ticket """
        try:
            result = update("tickets", {"id": id}, {"is_finished": "true"})
        except:
            message = "Error"
            result = "Something went wrong"
            http_status = 500
        else:
            message = "Success"
            http_status = 200
        finally:
            return {message: result}, http_status
