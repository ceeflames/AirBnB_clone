#!/usr/bin/python3


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created = datetime.now()
        self.updated = datetime.now()

    def save(self):
        self.updated = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created'] = self.created.isoformat()
        obj_dict['update'] = self.updated.isoformat()

        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__)
