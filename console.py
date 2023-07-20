#!/usr/bin/python3
"""Command Line Interface"""
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json
import re
import sys
import cmd
import os


class CommandLine(cmd.Cmd):
    """
    Mengist's AirBnB clone console application
    """

    intro = "Welcom to AirBnB Console "
    prompt = "(hbnb) "

    def do_exit(self, arg):
        """ >>> exit to exit"""
        sys.exit()

    def do_quit(self, arg):
        """ >>> quit to exit"""
        sys.exit()

    def do_EOF(self, arg):
        """End of File"""
        pass

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": State,
        "Review": Review,
        "Amenity": Amenity
    }


if __name__ == "__main__":
    CommandLine().cmdloop()
