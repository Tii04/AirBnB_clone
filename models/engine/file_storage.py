#!/bin/bash/python3
""" defines a class that stores files."""

from json import dump, load, dumps
from os.path import exists
from models import base_model


BaseModel = base_model.BaseModel
name_class = ["BaseModel", "City", "State",
                      "Place", "Amenity", "Review", "User"]



class FileStorage():
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary of class objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        class_name = obj.__class__.__name__

        id = obj.id

        class_id = class_name + '.' + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        dict_to_json = {}

        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            dump(dict_to_json, f)

    def reload(self):
        """ eserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""

        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                dic_obj = load(f)
                for key, value in dic_obj.items():
                    class_name = key.split(".")[0]
                    if class_name in name_class:
                        FileStorage.__objects[key] = eval(class_name)(**value)
                    else:
                        pass
