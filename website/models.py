#!/usr/bin/python3
"""Model to create database parameters"""

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Coord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longi = db.Column(db.String(150))
    latit = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    role = db.Column(db.String(60))
    coord  = db.relationship('Coord')
