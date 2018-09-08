from flask_script import Manager,Server
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# Creating app instance
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
# Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)


    return app