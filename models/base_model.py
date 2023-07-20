#!/usr/bin/python3
"""
This class defines BaseModel class
a base class for other object classes
"""
import models
import uuid
from uuid import uuid4

class BaseModel:
    """
    Base model for all classes of AirBnB console Project
    

    Args:
        id(str) - user identity number
        created_at(datetime) - time stamp of for created object
        updated_at(datetime) - time stamp for updating object
    """

    def __init__(self,  *args, **kwargs):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """getter method for id"""
        return self.__id

    @id.setter
    def id(self):
        """setter method for id"""
        self.__id = str(uuid.uuid4())

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self):
        self.__created_at = datetime.now()
    
    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self):
        self.__updated_at = datetime.now()
    

    def __str__(self):
        """ Returns string representation of a class"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"
    def __dict__(self):
        pass


    def save(self):
        pass

    def to_dict(self):
        pass

    