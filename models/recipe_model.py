from sqlalchemy import *
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB

from models import db

class Recipe(db.Model):
    __tablename__= "recipes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    description = db.Column(db.String(500))
    lastMade = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.String(700))
    imageURL = db.Column(db.String(200))
    ingredientList = db.Column(MutableDict.as_mutable(JSONB))
    cookingSteps = db.Column(MutableDict.as_mutable(JSONB))
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
            'ingredientList': self.ingredientList,
            'cookingSteps': self.cookingSteps,
            'dateAdded': self.dateAdded,
            'dateEdited': self.dateEdited
        }