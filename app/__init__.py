from flask import Flask

from app.controllers import main, auth
from app.extensions import database, authentication
from app.models import doodoo, user  # noqa: F401
from app.config import Config


def create_app_simple():
    app = Flask(__name__)

    return app


def create_app(config_instance: Config):
    app = Flask(__name__)

    app.config.from_object(config_instance)

    # Register the controllers
    main.init_app(app)
    auth.init_app(app)

    # Register the extensions
    database.init_app(app)
    authentication.init_app(app)

    return app
