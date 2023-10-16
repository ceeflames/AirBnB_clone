#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """
    The review model inherets the BaseModel
    with public class attr
    """
    place_id = ""
    user_id = ""
    text = ""
