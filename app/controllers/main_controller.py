from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity


main = Blueprint('main', __name__)


@main.route('/')
@jwt_required()
def index():
    current_user = current_identity

    print(current_user)

    return "Hello, World!"


def init_app(app: Flask):
    app.register_blueprint(main)
