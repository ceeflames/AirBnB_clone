#!/usr/bin/python3


"""
 Module documentation.
 Import and use the classes defined in this module.
"""


import models
import uuid
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String


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
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the updated_at public instance attribute 
        with the current time datetime.

        Call the save methos of the storage instance
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        This function returns a dictionary representation
        of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = str(type(self).__name__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict.pop("_sa_instance_state", None)

        return obj_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        j = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__,
                self.id, j)
