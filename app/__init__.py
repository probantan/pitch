from flask_script import Manager,Server
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
# Creating app instance
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
# Initializing Flask Extensions
    bootstrap.init_app(app)


    return app