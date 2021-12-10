import datetime
# from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

class AppointmentModel():
    def __init__(self, date, time, duration, ticketId, isFinished):
        self.id = self.new_id()
        self.date = date
        self.time = time
        self.duration = duration
        self.ticketId = ticketId
        self.isFinished = isFinished

class AppointmentSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    duration = fields.Str(required=True)
    ticketId = fields.Integer(required=True)
    isFinished = fields.Boolean(default=False)
