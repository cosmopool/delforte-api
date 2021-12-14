from marshmallow import Schema, fields

from zione.appointments.model import AppointmentSchema
from zione.tickets.model import TicketSchema

class AppointmentModel():
    def __init__(self, date, time, duration, ticketId, clientName, clientPhone, clientAddress, serviceType, description):
        # self.id = self.new_id()
        ticket = {
                'clientName': clientName,
                'clientAddress': clientAddress,
                'clientPhone': clientPhone,
                'serviceType': serviceType,
                'description': description
                }

        appointment = {
                'date': date,
                'time': time,
                'duration': duration,
                'ticketId': ticketId
                }

        self.ticket = TicketSchema().load(ticket)
        self.appointment = AppointmentSchema(partial=True).load(appointment)

class AppointmentSchema(Schema):
    ticket = fields.Nested(TicketSchema)
    appointment = fields.Nested(AppointmentSchema)

# class AppointmentModel():
#     def __init__(self, date, time, duration, ticketId, isFinished, address, clientName, clientPhone, clientAddress, serviceType, description):
#         # self.id = self.new_id()
#         self.date = date
#         self.time = time
#         self.duration = duration
#         self.ticketId = ticketId
#         self.isFinished = isFinished
#         self.address = address
#         self.clientName = clientName
#         self.clientAddress = clientAddress
#         self.clientPhone = clientPhone
#         self.serviceType = serviceType
#         self.description = description

# class AppointmentSchema(Schema):
#     # id = fields.Integer(required=False)
#     date = fields.Date(required=True)
#     time = fields.Time(required=True)
#     duration = fields.Str(required=True)
#     ticketId = fields.Integer(required=True)
#     isFinished = fields.Boolean(default=False)
#     address = fields.Str(required=True)
#     clientName = fields.Str(required=True)
#     clientPhone = fields.Str(required=True)
#     serviceType = fields.Str(required=True)
#     description = fields.Str(required=True)
