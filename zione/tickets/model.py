from marshmallow import Schema, fields

class TicketModel():
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
