from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(strict=True, default=-1, required=False)
    username = fields.Str(strict=True, required=True)
    password = fields.Str(strict=True, required=True)
