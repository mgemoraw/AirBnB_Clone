import cmd
import sys
import os


class Down(cmd.Cmd):
    def cmdloop(self, intro=None):
        print("cmdloop(%s)"%intro)
        return cmd.Cmd.cmdloop(self, intro)
    def do_greet(self, arg):
        """greet [person name]
        >>> greet Alex
        Hello, Alex. How do you do?
        """
        print("Hello, {0}. How do you do?".format(arg))
    def do_cd(self, path):
        pass
        
    def do_ls(self, arg):
        for f in os.listdir():
            print(f)
    def do_bye(self, arg):
        sys.exit()


if __name__ == "__main__":
    Down().cmdloop()