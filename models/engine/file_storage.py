#!/usr/bin/python3


"""This is a documentation for the FileStorage class."""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class that serializes insatnces to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects.

        Returns:
            dicts: a dictionary containing all objects stored by
            <classs name>.id.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict

        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with the key  <obj class name>.id.
        Args:
            obj: An instance of a class to be stored.
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj


    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        odict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)


    def reload(self):
        """
        Deserializes the JSON file to __objects if the file (__file_path) exists.

        if the file doesn't exist, no exception shoild be raised.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data.values():
                    if '__class__' in i:
                        name = i['__class__']
                        del i['__class__']
                        self.new(eval(name)(**i))
                    else:
                        pass

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects if the objects already exists
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call reload method"""
        self.reload()
