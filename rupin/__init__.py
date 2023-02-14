from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from .home import home

        app.register_blueprint(home.home_bp)

        return app
