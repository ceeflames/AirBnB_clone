#!/usr/bin/python3
"""
The BaseModel class defines all of the common
attributes and methods for other classes.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Creates a BaseModel Class from which other
    classes will inherit.
    """

    def __init__(self, *args, **kwargs):
        """create a new BaseModel object."""

        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the object's string representation."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Saves to json and updates to the current time."""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all of the instance's
        key/value pairs."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                v = self.__dict__[k].isoformat()
                my_dict[k] = v
        return my_dict
