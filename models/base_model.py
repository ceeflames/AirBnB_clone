#!/usr/bin/python3


"""
 Module documentation.
 Import and use the classes defined in this module.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel is a base class with common attributes and methods.

    Public instance attr:
        id (str): Unique identifier generated using uuid.uuid4()
        created_at (datetime): The timestamp when the instance is created.
        updated_at (datetime): Timestamp when the instance is last updated.

    Public instance methods:
        save(self): Updates the updated_at attr with the current datetime
        to_dict(self): Returns a dictionary representation of the instance

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Upon initialization the public instance attributes are set.

        if kwargs is not empty:
        - Each key of the kwargs dictionary is an attribute name
        - Note: '__class__' from kwargs is not added as an attribute
        - Each value of the kwargs dictionary is the value of the
            corresponding attribute.

        if kwargs is empty:
        - create 'id' and 'created_at' attributes as in the previous constructor

        Args:
            *args: Unused.
            **kwargs: Dictionary containing attribute name-value pairs

        Call the new methos on the storage instance for new instances
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.now()
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at public instance attribute 
        with the current time datetime.

        Call the save methos of the storage instance
        """
        self.updated = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This function returns a dictionary representation
        of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__)
