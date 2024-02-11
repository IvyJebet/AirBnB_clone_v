#!/usr/bin/python3
"""Module that serializes instances to a JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Class used to store, serialize and deserialize data"""
    __file_path = "file.json"
    __objects = {}


    def new(self, obj):
        """Public instance method that sets in __objects the obj with key"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Public instance method that returns the dictionary __objects"""
        return  FileStorage.__objects

    def save(self):
        """Public instance method that serializes __objects to the JSON file"""
        all_objects = FileStorage.__objects
        objects_dict = {}

        for obj_key, obj_value in all_objects.items():
            objects_dict[obj_key] = obj_value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Public instance method that deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for obj_key, obj_value in obj_dict.items():
                        class_name, obj_id = obj_key.split('.')
                        cls = eval(class_name)
                        instance = cls(**obj_value)
                        FileStorage.__objects[obj_key] = instance
                except Exception:
                    pass
