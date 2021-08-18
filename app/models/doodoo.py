#  type: ignore
"""..."""
from datetime import datetime

from app.models.user import User
from app.extensions.database import db


class DooDoo(db.Model):
    __tablename__ = 'doodoos'
    id = db.Column(db.Integer, primary_key=True)
    doodoo = db.Column(db.String(256))
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    claps = db.Column(db.Integer, default=0)
    redooits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # TODO: Add original_user_id field to keep track the original post's owner

    def __init__(self, doodoo: str, user_id: int) -> None:
        self.doodoo = doodoo
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def add_claps(self):
        self.claps += 1
        db.session.commit()

    def add_redooits(self):
        self.redooits += 1
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'doodoo': self.doodoo,
            'posted': self.posted,
            'claps': self.claps,
            'redooits': self.redooits,
            'user': User.query.get(self.user_id).username
        }

    def __repr__(self):
        return '<DooDoo %r>' % self.doodoo
