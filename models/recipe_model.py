from sqlalchemy import *

from models import db

class Recipe(db.Model):
    __tablename__= "recipes"
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    description = db.Column(db.String(500))
    lastMade = db.Column(db.DateTime)
    notes = db.Column(db.String(700))
    imageURL = db.Column(db.string(200))
    dateAdded = db.Column(db.DateTime, server_default=func.now())
    dateEdited = db.Column(db.String(100))

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'nationality': self.nationality,
            'description': self.description,
            'lastMade': self.lastMade,
            'notes': self.notes,
            'imageURL': self.imageURL,
            'dateAdded': self.dateAdded,
            'dateEdited': self.dateEdited
        }