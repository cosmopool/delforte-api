import datetime
from marshmallow import Schema, fields

class AppointmentModel():
    def __init__(self, date, time, duration, ticket_id, is_finished, address):
        self.id = self.new_id()
        self.date = date
        self.time = time
        self.duration = duration
        self.ticket_id = ticket_id
        self.is_finished = is_finished
        self.address = address
        self.client_name = client_name
        self.client_phone = client_phone
        self.service_type = service_type
        self.description = description

class AppointmentSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    duration = fields.Str(required=True)
    ticket_id = fields.Integer(required=True)
    is_finished = fields.Boolean(default=False)
    address = fields.Str(required=True)
    client_name = fields.Str(required=True)
    client_phone = fields.Str(required=True)
    service_type = fields.Str(required=True)
    description = fields.Str(required=True)
