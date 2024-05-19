# Import Flask to create the application instance
from flask import Flask
# Import the configuration class for development environment settings
from config import DevelopmentConfig
# Import SQLAlchemy for database interactions
from flask_sqlalchemy import SQLAlchemy
# Import Migrate to handle SQLAlchemy database migrations
from flask_migrate import Migrate
# Import LoginManager for handling user authentication
from flask_login.login_manager import LoginManager

# Create a SQLAlchemy object instance for database operations
db = SQLAlchemy()
# Create a LoginManager object instance for managing user logins
login = LoginManager()
# Set the default view for login (redirect to 'main.login' when unauthorized users access protected views)
login.login_view = 'main.login'


def create_app(config_class=DevelopmentConfig):
    # Create the Flask app instance
    app = Flask(__name__)
    # Load configuration from the config class provided
    app.config.from_object(config_class)
    # Initialize SQLAlchemy with app instance
    db.init_app(app)
    # Initialize LoginManager with app instance
    login.init_app(app)
    
    # Import the 'main' blueprint from the blueprints package
    from app.blueprints import main
    # Register the 'main' blueprint with the app
    app.register_blueprint(main)

    # Return the app instance to be used by the WSGI server
    return app

# Import models and api modules (These imports might be for models and api initialization)
from app import models, api
