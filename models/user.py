#!/usr/bin(BaseModel)/python3
""" A user class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel

    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
