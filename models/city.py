#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """The city class inherets from BaseModel"""
    state_id = ""
    name = ""
