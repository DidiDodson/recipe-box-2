from sqlalchemy import ForeignKey, String, Column

from models import db

class RecipeIngredient(db.Model):
    __tablename__= "recipe_ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipeId = db.mapped_column(db.Integer, ForeignKey("recipes.id"))
    ingredientId = db.mapped_column(db.Integer, ForeignKey("ingredients.id"))

    def json(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'ingredientId': self.ingredientId
        }    

