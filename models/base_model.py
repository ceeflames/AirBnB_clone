#!/usr/bin/python3


"""
 Module documentation.
 Import and use the classes defined in this module.
"""


import uuid
from datetime import datetime


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
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Upon initialization the public instance attributes are set.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the updated_at public instance attribute 
        with the current time datetime.
        """
        self.updated = datetime.now()

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
