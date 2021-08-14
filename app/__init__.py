from flask import Flask

from app.controllers import main, auth
from app.config import Config


def create_app(config_instance: Config):
    app = Flask(__name__)

    app.config.from_object(config_instance)

    # Register the controllers
    main.init_app(app)
    auth.init_app(app)

    return app
