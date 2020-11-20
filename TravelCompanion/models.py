from TravelCompanion import db
from sqlalchemy.dialects.postgresql import JSON

class Airport(db.Model):
    __tablename__ = 'Flights'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String())

    def __init__(self, Name):
        self.Name = Name

    def __repr__(self):
        return {
            'id': self.ID, 
            'name': self.Name
            }

    def serialize(self):
        return {
            'id': self.ID, 
            'name': self.Name
            }