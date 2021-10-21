# import db
from db import insert, select, delete, update
from flask import request
from flask_restful import Resource, reqparse
from .model import TicketSchema

class TicketOpen(Resource):
    def get(self):
        """ Get all open tickets """
        try:
            result = select("tickets", {"is_finished": "false"})
        except:
            result = "something went wrong searching your data"
            http_status = 500
        else:
            http_status = 200
        finally:
            return {"open tickets": result}, http_status

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
                result = "something went wrong writing your data"
                http_status = 500
            else:
                http_status = 200
        finally:
            return {"message": result}, http_status

class Tickets(Resource):
    def get(self, id):
        """ Get information about specific ticket """
        schema = TicketSchema()
        try:
            result = select("tickets", {"id": id})
        except KeyError:
            result = "no record found with given id"
            http_status = 400
        except:
            result = "something went wrong while searching your data"
            http_status = 500
        else:
            result = schema.load(result[0])
            http_status = 200
        finally:
            return {"message": result}, http_status

    def patch(self, id):
        """ Edit a specific ticket """
        schema = TicketSchema(partial=True)
        ticket = schema.load(request.json)
        try:
            ticket = self.__val_ticket__(ticket, id)
        except ValueError:
            result = "id do not match"
            http_status = 406
        except ValidationError:
            result = "error validating your data"
        else:
            try:
                result = update("tickets", {"id": id}, ticket)
            except:
                result = "value too long"
                http_status = 409
            else:
                if result == 0:
                    http_status = 406
                else:
                    http_status = 200
        finally:
            return {"message": result}, http_status

    def delete(self, id):
        """ Delete a specific ticket """
        schema = TicketSchema()
        result = delete("tickets", {"id": id})

        if result == 0:
            http_status = 404
        else:
            http_status = 200

        return { "message": result }, http_status

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
    def post(self, id):
        """ Close a open ticket """
        schema = TicketSchema()
        pass
