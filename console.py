#!/usr/bin/python3
""" Command interpreter for the console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Airbnb command line interpreter """
    def __init__(self):
        self.prompt = '(hbnb) '
        self.completekey = 'tab'
        super().__init__()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
