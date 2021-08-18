from app.models.user import User
from flask import blueprints
from flask.app import Flask


auth = blueprints.Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "login page"


@auth.route('/logout')
def logout():
    return "logout page"


@auth.route('/register')
def register():
    user = User(username='test', password='test', email='test@test')
    user.save()
    return "register page"


def init_app(app: Flask):
    app.register_blueprint(auth, url_prefix='/auth')
