#!/usr/bin/python3
""" Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseMode

    Attributes:
        place_id (str): it will be Place.id
        user_id (str): it will be User.id
        text (str): text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """ initializes Review class """
        super().__init__(self)
