from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User <{self.username}>"


class BlogPost(db.Model):
    """This is the blogpost database model"""

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    author = db.Column(db.Text)
