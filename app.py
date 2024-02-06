from flask import Flask
from flask_cors import CORS
import os
from models import db

def create_app():

    app = Flask(__name__, static_folder='build')
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #  import models    
    import models.ingredient_model
    import models.recipe_model
    import models.recipe_ingredient_model

    with app.app_context():
        db.create_all()

    from api_routes import api

    app.register_blueprint(api, url_prefix='/api')    
        
    @app.before_request
    def before_request():
        app.jinja_env.cache = {}    

    app.before_request(before_request)     
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)