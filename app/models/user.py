#  type: ignore
"""..."""
from datetime import datetime

from app.extensions.database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(128), unique=True)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.utcnow)
    doodoos = db.relationship('DooDoo', backref='users', lazy=True)
    password = db.Column(db.String(128))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }

    def __repr__(self):
        return '<User %r>' % self.username
