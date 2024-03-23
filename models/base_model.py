#!/usr/bin/python3
""" Base for all the other classes """
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base class for all models.

    Attributes:
        id (str): Unique identifier for the model instances
        created_at (datetime): time instance was created
        updated_at (datetime): time instance was updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if kwargs:
            for key in kwargs.keys():
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(kwargs[key])
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(kwargs[key])
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns:
            str: A string representation of the model instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def name(self, arg):
        """
        Sets the name attribute of the model instance

        Args:
            arg: The value to set as the new attribute
        """
        self.name = arg

    def my_number(self, arg):
        """
        Sets the my_number attribute of the model instance

        Args:
            arg: The value to set to my_number attribute
        """
        self.my_number = arg

    def save(self):
        """ Updates the updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the model instance to a dictionary

        Returns:
            dict: A dictionary representation of the model instance
        """
        d = self.__dict__.copy()
        d.update({'__class__': self.__class__.__name__})
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
