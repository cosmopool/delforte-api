from marshmallow import Schema, fields

class TicketModel():
    def __init__(self, id, clientName, clientAddress, clientPhone, serviceType, description, isFinished):
        # self.id = self.__new_id__()
        self.id = id
        self.clientName = clientName
        self.clientAddress = clientAddress
        self.clientPhone = clientPhone
        self.serviceType = serviceType
        self.description = description
        self.isFinished = isFinished

class TicketSchema(Schema):
    id = fields.Integer()
    clientName = fields.Str(required=True)
    clientAddress = fields.Str(required=True)
    clientPhone = fields.Str(required=True)
    serviceType = fields.Str(required=True)
    description = fields.Str(required=True)
    isFinished = fields.Boolean(default=False)
