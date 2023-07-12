from base import BaseModel


class User(BaseModel):
    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:
            self.__id = 0
        else:
            self.__id = value
    @classmethod
    def id(self, value):
        if self.id is not None:
            self.id += 1
        else:
            self.id = 0


