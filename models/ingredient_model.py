from sqlalchemy import *

from models import db

class Ingredient(db.Model):
    __tablename__= "ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    dateAdded = db.Column(db.DateTime, server_default=func.now())
    dateEdited = db.Column(db.String(100))

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'dateAdded': self.dateAdded,
            'dateEdited': self.dateEdited
        }