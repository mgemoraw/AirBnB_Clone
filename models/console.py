#!/usr/bin/python3
from user import User

import sys
import cmd
import os


class CommandLine(cmd.Cmd):
    intro = "Welcom to AirBnB Console App"
    prompt = "(hbnb) "
    def do_user(self, arg):
        "creates user class"
        user = User()
        print(user.id)

    def do_exit(self, arg):
        """ >>> exit to exit"""
        sys.exit()

    def do_quit(self, arg):
        """ >>> quit to exit"""
        sys.exit()
    def do_EOF(self,arg):
        """End of File"""
        pass

if __name__ == "__main__":
    CommandLine().cmdloop()