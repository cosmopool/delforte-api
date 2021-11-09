import datetime
# from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

class AppointmentModel():
    def __init__(self, date, time, duration, ticket_id, is_finished):
        self.id = self.new_id()
        self.date = date
        self.time = time
        self.duration = duration
        self.ticket_id = ticket_id

class AppointmentSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    duration = fields.Str(required=True)
    ticket_id = fields.Integer(required=True)
