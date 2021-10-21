from marshmallow import Schema, fields

class UserModel():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str()
    password = fields.Str()

