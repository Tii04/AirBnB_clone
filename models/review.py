#!/usr/bin/python3
""" A class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ This class city inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
