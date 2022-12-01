#!/usr/bin/bash/python3
""" Defines a class that inherits from BaseModel"""

from models.base_model import BaseModel
import uuid


class User(BaseModel):
    """ User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

