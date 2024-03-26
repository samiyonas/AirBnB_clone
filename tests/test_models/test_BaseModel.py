#!/usr/bin/python3
""" Unit test for my class BaseModel """
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Class that tests our BaseModel """
    base = BaseModel()
    def test_attrs(self):
        """ This test tests Attributes """
        my_base_dict = self.base.to_dict()

        self.assertEqual(self.base.id, my_base_dict['id'])

    def test_save(self):
        """ This test tests save method """
        self.base.save()

        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

        my_dict = self.base.to_dict()
        self.base.save()

        my_dict1 = self.base.to_dict()

        self.assertEqual(my_dict['created_at'], my_dict1['created_at'])
        self.assertNotEqual(my_dict['updated_at'], my_dict1['updated_at'])

if __name__ == "__main__":
    unittest.main()
