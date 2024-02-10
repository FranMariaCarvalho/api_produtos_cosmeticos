from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource, fields
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app, version='1.0', title='API de Produtos Cosméticos',
          description='Uma API para gerenciamento de produtos')

from app.models.models import Produto
from app.controllers.produto_controllers import *
