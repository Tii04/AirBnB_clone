#!/usr/bin/python3
"""This class defines all attributes for other classes"""


from uuid import uuid4
from datetime import datetime
import json
import models


class BaseModel():
    """ This class defines all attributes for other classes that
        inherit it."""

    def __init__(self, *args, **kwargs):
        """ Initialises attributes"""

        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)

        else:

            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Specifies the format of printing"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """  returns a dictionary containing all
        keys/values of __dict__ of the instance"""

        dictt = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dictt[key] = item

        dictt['__class__'] = self.__class__.__name__
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()

        return dictt
