from flask import Blueprint
from flask.app import Flask


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Hello, World!"


def init_app(app: Flask):
    app.register_blueprint(main)
