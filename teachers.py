# User model
from flask_login import UserMixin
from __init__ import db

class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    session_token = db.Column(db.String(500), nullable=True)

