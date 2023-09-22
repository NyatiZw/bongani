#!/usr/bin/python
"""holds class Mappoints"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Mappoints(BaseModel, Base):
    """Representation of MapPoints"""
    if models.storage_t == 'db':
        __tablename__ = 'mappoints'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Mappoints"""
        super().__init__(*args, **kwargs)
