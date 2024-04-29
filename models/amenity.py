#!/usr/bin/python3
"""The `amenity` module

It defines one class, `Amenity(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """The amenity class, contains name field and places relationship.
    """
    __tablename__ = "amenities"
    name = Column('name', String(128), nullable=False)
