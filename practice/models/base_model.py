#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:

    """
    A constructor with public instance attributes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """
    prints:[<class name>](<self.id>)<self.__dict__>
    """
    def __str__(self):
        return "[{}]({}){}".format(
                self.__class__.__name__, self.id, self.__dict__)
    """
    updates the public instance attribute updated_at with the current datetime
    """
    def save(self):
        self.updated_at = datetime.now()

    """
    returns a dictionary containing all keys/values of __dict__ of the instance
    """
    def to_dict(self):
        inst_dict = self.__dict__
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict


# check if Python script is being run as the main program
if __name__ == "__main__":
    # Create an instance of BaseModel
    obj1 = BaseModel()

    # Call to_dict method on the instance
    obj1.to_dict()
