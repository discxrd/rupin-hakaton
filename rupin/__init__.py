from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=False)

app.config.from_object("config.Config")

login_manager = LoginManager()
login_manager.login_view = "auth.sign_in"
login_manager.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .home import home
from .api import api
from .auth import auth

app.register_blueprint(home.home_bp)
app.register_blueprint(api.api_bp)
app.register_blueprint(auth.auth_bp)
