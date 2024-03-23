#!/usr/bin/python3
""" File storage engine of our objects """
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ File storage class

    Attributes:
        __objects (dict): will store all objects
        __file_path (str): path to the JSON file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns:
            the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects.update({obj.__class__.__name__+'.'+obj.id: obj})

    def save(self):
        """ serializes __objects to the JSON file """
        todict = {i: j.to_dict() for i, j in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(todict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = None
                try:
                    temp = json.load(f)
                except Exception:
                    pass
                if temp is None:
                    return
                FileStorage.__objects = {
                        i: BaseModel(**j) for i, j in temp.items()}
        except Exception:
            pass
