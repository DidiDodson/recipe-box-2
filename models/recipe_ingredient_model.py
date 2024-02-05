from sqlalchemy import ForeignKey, String, Column

from models import db

class RecipeIngredient(db.Model):
    __tablename__= "recipe_ingredients"
    id = db.Column(db.String(100), primary_key=True)
    recipeId = db.mapped_column(db.String, ForeignKey("recipes.id"))
    ingredientId = db.mapped_column(db.String, ForeignKey("ingredients.id"))

    def json(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'ingredientId': self.ingredientId
        }    

