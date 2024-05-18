from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'main.login'


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login.init_app(app)
    
    from app.blueprints import main
    app.register_blueprint(main)

    return app

from app import models, api