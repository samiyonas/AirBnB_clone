#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits from BaseModel

    Attributes:
        name (str): name
    """
    name = ""
