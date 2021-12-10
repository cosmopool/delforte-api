from marshmallow import Schema, fields

class AppointmentModel():
    def __init__(self, date, time, duration, ticketId, isFinished, address):
        self.id = self.new_id()
        self.date = date
        self.time = time
        self.duration = duration
        self.ticketId = ticketId
        self.isFinished = isFinished
        self.address = address
        self.clientName = clientName
        self.clientPhone = clientPhone
        self.serviceType = serviceType
        self.description = description

class AppointmentSchema(Schema):
    id = fields.Integer()
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    duration = fields.Str(required=True)
    ticketId = fields.Integer(required=True)
    isFinished = fields.Boolean(default=False)
    address = fields.Str(required=True)
    clientName = fields.Str(required=True)
    clientPhone = fields.Str(required=True)
    serviceType = fields.Str(required=True)
    description = fields.Str(required=True)
