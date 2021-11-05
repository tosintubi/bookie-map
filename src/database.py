import string
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import random

db = SQLAlchemy


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.Text, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref='user')

    def __repr__(self):
        return f'User ({self.username})'


class Bookmark(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(3), nullable=True)
    visits = db.Column(db.Integer, default=0)
    # User id Foreignkey
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_characters(self):
        characters = string.digits + string.ascii_letters
        selected_characters = ''.join(random.choices(characters, k=3))

        link = self.query.filter_by(short_url=selected_characters).first()

        # If the characters already exist in db, rerun generate_characters again
        if link:
            self.generate_characters()
        else:
            return  selected_characters
