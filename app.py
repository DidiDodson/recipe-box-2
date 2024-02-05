from flask import Flask, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from models import db


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    import models.ingredient_model

    with app.app_context():
        db.create_all()

    # @app.route("/hello/")
    # @app.route("/hello/<name>")
    # def hello(name=None):
    #     return render_template('hello.html', name=name)

    @app.route("/")
    def index():
        return render_template('hello.html')
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)