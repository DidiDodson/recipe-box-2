from flask import Blueprint, current_app, send_from_directory, render_template, make_response, jsonify, request
import json

from models import db

from models.ingredient_model import Ingredient
from models.recipe_model import Recipe

app = current_app
api = Blueprint('api', __name__)
    
@api.route("/")
def homepage():

    return render_template('hello.html') 

@api.route('recipes', methods=['GET'])
def get_recipes():
    try: 
        recipes = Recipe.query.order_by(Recipe.name).all()

        return make_response(jsonify([recipe.json() for recipe in recipes]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting recipes'}), 500)    

@api.route('recipes/<id>', methods=['GET'])
def get_recipe(id):
    try: 
        recipe = Recipe.query.filter_by(id=id).first()

        return make_response(jsonify({'recipe': recipe.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting recipe'}), 500)
    
@api.route('ingredients', methods=['GET'])
def get_ingredients():
    try: 
        ingredients = Ingredient.query.order_by(Ingredient.name).all()

        return make_response(jsonify([ingredient.json() for ingredient in ingredients]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting ingredients'}), 500)
    
@api.route('ingredients/<id>', methods=['GET'])
def get_ingredient(id):
    try: 
        recipe = Recipe.query.filter_by(id=id).first()

        return make_response(jsonify({'recipe': recipe.json()}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting recipe'}), 500)    