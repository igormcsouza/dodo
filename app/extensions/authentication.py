from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

from app.models.user import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and safe_str_cmp(user.password.encode('utf-8'),
                             password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.get(user_id)


jwt = JWT(authentication_handler=authenticate, identity_handler=identity)


def init_app(app):
    jwt.init_app(app)
