from TravelCompanion import db
from sqlalchemy.dialects.postgresql import JSON

class Airport(db.Model):
    __tablename__ = 'Flights'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, Name):
        self.Name = Name

    def __repr__(self):
        return '<id {}>'.format(self.ID)

    def serialize(self):
        return {
            'id': self.ID, 
            'name': self.Name
            }