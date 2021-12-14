from marshmallow import Schema, fields

class TicketModel():
<<<<<<< HEAD
    def __init__(self, id, client_name, client_address, client_phone, service_type, description, is_finished):
        # self.id = self.__new_id__()
        self.id = id
        self.client_name = client_name
        self.client_address = client_name
        self.client_phone = client_phone
        self.service_type = service_type
        self.description = description
        self.is_finished = is_finished

class TicketSchema(Schema):
    id = fields.Integer()
    client_name = fields.Str(required=True)
    client_address = fields.Str(required=True)
    client_phone = fields.Str(required=True)
    service_type = fields.Str(required=True)
    description = fields.Str(required=True)
    is_finished = fields.Boolean(default=False)
=======
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
>>>>>>> feature/address-geocoding
