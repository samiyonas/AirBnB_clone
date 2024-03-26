#!/usr/bin/python3
""" State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits from BaseModel

    Attributes:
        name (str): name a state
    """
    name = ""
