#!/usr/bin/python3
""" A class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """ This class city inherits from BaseModel"""

    state_id = ""
    name = ""
