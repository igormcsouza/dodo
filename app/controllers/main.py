from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required


main = Blueprint('main', __name__)


@main.route('/')
@jwt_required()
def index():
    return "Hello, World!"


def init_app(app: Flask):
    app.register_blueprint(main)
