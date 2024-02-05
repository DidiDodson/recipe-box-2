from flask import Blueprint, current_app, send_from_directory, render_template

from models import db

from models.ingredient_model import Ingredient
from models.recipe_model import Recipe

app = current_app
api = Blueprint('api', __name__)
    
@api.route("/")
def index():
    recipes = Recipe.query.all()

    return render_template('hello.html', recipes=recipes)    