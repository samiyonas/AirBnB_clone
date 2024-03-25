#!/usr/bin/python3
""" Command interpreter for the console """
import cmd
from datetime import datetime
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Airbnb command line interpreter """
    def __init__(self):
        """ initializes the command instance """
        self.prompt = "(hbnb) "

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        if line == "BaseModel":
            tok = line + "()"
            my_model = eval(tok)
            print(my_model.id)
            storage.save()

    def do_show(self, line):
        """
        prints the string representation of an instance
        Based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 2:
            return
        else:
            all_objs = storage.all()
            k = "{}.{}".format(args[0], args[1])
            for keys in all_objs:
                if keys == k:
                    print(all_objs[keys])
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        Change is saved into the JSON file
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 2:
            return
        else:
            all_objs = storage.all()
            k = "{}.{}".format(args[0], args[1])
            for keys in all_objs:
                if keys == k:
                    del all_objs[keys]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """
        prints all string representation of all instances
        based or not on the class name
        """
        if line and line != "BaseModel":
            print("** class doesn't exist **")
        elif not line or line == "BaseModel":
            all_objs = storage.all()
            obj = [str(j) for i, j in all_objs.items()]
            print(obj)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        Change is saved into JSON file.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            all_objs = storage.all()
            k = "{}.{}".format(args[0], args[1])
            if k not in all_objs.keys():
                print("** no instance found **")
                return
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[3].startswith('"') and args[3].endswith('"'):
                args[3] = args[3][1:-1]
            ojb = all_objs[k]
            ojb.__dict__[args[2]] = args[3]
            ojb.updated_at = datetime.now()
            storage.save()

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
