# from db import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AppointmentModel(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    is_finished = db.Column(db.Boolean)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
