#!/usr/bin/python3


"""This is a documentation for the FileStorage class."""


import json


class FileStorage:
    """
    FileStorage class that serializes insatnces to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dicts: a dictionary containing all objects stored by
            <classs name>.id.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with the key  <obj class name>.id.

        Args:
            obj: An instance of a class to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_data, f)


    def reload(self):
        """
        Deserializes the JSON file to __objects if the file (__file_path) exists.

        if the file doesn't exist, no exception shoild be raised.
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_name = class_name
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
