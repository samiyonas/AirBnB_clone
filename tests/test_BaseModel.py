#!/usr/bin/python3
""" This module handles miscellaneous unit testing """

import os
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class defines a series of test
    for the Airbnb console
    """

    base = BaseModel()

    def test_BaseModelTest_1(self):
        """ This tests Attributes """
        self.base.save()
        todict = self.base.to_dict()

        self.assertEqual('BaseModel', todict['__class__'])
        self.assertEqual(self.base.id, todict['id'])

    def test_Save(self):
        """ This tests save method """
        self.base.save()

        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

        my_dict = self.base.to_dict()

        self.base.save()
        my_dict1 = self.base.to_dict()

        self.assertEqual(my_dict['created_at'], my_dict1['created_at'])
        self.assertNotEqual(my_dict['updated_at'], my_dict1['updated_at'])


if __name__ == '__main__':
    unittest.main()
