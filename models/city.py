#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel

    Attributes:
        state_id (str): state id
        name (str): name of the City
    """
    state_id = ""
    name = ""
