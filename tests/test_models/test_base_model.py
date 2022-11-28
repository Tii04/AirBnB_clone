#!/usr/bin/python3

""" Test cases for models"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


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

    def test_time_diff_created_at(self):
        """Tests if there is a time difference"""

        instance1 = BaseModel()
        sleep(1)
        instance2 = BaseModel()
        self.assertNotEqual(instance1.created_at, instance2.created_at)

    def test_time_diff_updated_at(self):
        """ Tests for time difference"""

        instance1 = BaseModel()
        sleep(1)
        instance2 = BaseModel()
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_baseModel(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_kwargs(self):
        basemodel = BaseModel()
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertFalse(hasattr(basemodel, "name"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

if __name__ == '__main__':
    unittest.main()
