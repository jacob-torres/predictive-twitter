"""Data models for the application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class UserTable(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    handle = db.Column(db.String(120), unique=True, nullable=False)


class TweetTable(db.Model):


