from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .home import home
from .api import api

app.register_blueprint(home.home_bp)
app.register_blueprint(api.api_bp)
