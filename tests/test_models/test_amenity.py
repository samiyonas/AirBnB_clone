#!/usr/bin/python3
""" This module handles miscellaneous unit testing """

import models
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_str_representation(self):
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(str(amenity), "[Amenity] ({}) {}"
                         .format(amenity.id, amenity.__dict__))


if __name__ == '__main__':
    unittest.main()
