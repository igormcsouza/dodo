from flask import Flask

from app.controllers import main, auth


def create_app(config_filename: str):
    app = Flask(__name__)

    app.config.from_object(config_filename)

    # Register the controllers
    main.init_app(app)
    auth.init_app(app)

    return app
