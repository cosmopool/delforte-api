from marshmallow import Schema, fields

from zione.domain.entities.appointment import Appointment


class AppointmentSchema(Schema):
    id = fields.Integer(strict=True, default=-1, required=False)
    # date = fields.Date(strict=True, required=True)
    # time = fields.Time(strict=True, required=True)
    # duration = fields.Time(strict=True, required=True)
    date = fields.Str(strict=True, required=True)
    time = fields.Str(strict=True, required=True)
    duration = fields.Str(strict=True, required=True)
    ticketId = fields.Integer(strict=True, required=True)
    isFinished = fields.Boolean(strict=True, default=False)

    def _make_instance(self, data):
        return Appointment(**data)
