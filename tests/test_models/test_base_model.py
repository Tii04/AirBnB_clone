#!/usr/bin/python3

""" Test cases for models"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test cases"""

    def test_docs(self):
        """ Checks for doc strings"""

        self.assertIsNotNone(BaseModel.__doc__)

    def test_created_at_type(self):
        """ Tests the type of created_at"""

        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        """ Tests the type of updated_at"""

        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_id_type(self):
        """ Tests the type of id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_instance_ids(self):
        """ Tests to see if ids are unique"""

        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
    

if __name__ == '__main__':
    unittest.main()
