# from db import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TicketModel(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String())
    client_phone = db.Column(db.String())
    service_type = db.Column(db.String(11))
    description = db.Column(db.Text)
    is_finished = db.Column(db.Boolean)
    appointment = db.relationship('AppointmentModel', backref='TicketModel', lazy=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
