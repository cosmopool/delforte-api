from marshmallow import Schema, fields

class TicketSchema(Schema):
    id = fields.Integer(strict=True, default=-1, required=False)
    clientName = fields.Str(required=True)
    clientAddress = fields.Str(required=True)
    clientPhone = fields.Int(required=True)
    serviceType = fields.Str(required=True)
    description = fields.Str(required=True)
    isFinished = fields.Boolean(default=False)
