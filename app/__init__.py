# app/__init__.py

from flask import Flask
from app.database import db
from flask_migrate import Migrate
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_projeto.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    Migrate(app, db)
    Swagger(app)
    
    from app.controllers.produto_controller import produto_blueprint
    app.register_blueprint(produto_blueprint)
    
    return app
