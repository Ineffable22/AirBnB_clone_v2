#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        store = {}
        for key, value in FileStorage.__objects.items():
            if value.__class__ == cls:
                store[key] = value
        return store

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel

        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                js = json.load(file)
            for key, value in js.items():
                reloadobj = classes[js[key]["__class__"]](**js[key])
                self.__objects[key] = reloadobj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects if it’s inside
        - if obj is equal to None """
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            del FileStorage.__objects[key]

    def close(self):
        """method to reload"""
        self.reload()
