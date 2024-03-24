#!/usr/bin/python3
""" Command interpreter for the console """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Airbnb command line interpreter """
    def __init__(self):
        """ initializes the command instance """
        self.prompt = '(hbnb) '
        self.completekey = 'tab'
        super().__init__()

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        if line == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
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
        if line and line != "BaseModel":
            print("** class doesn't exist **")
        elif not line or line == "BaseModel":
            all_objs = storage.all()
            l = [str(j) for i, j in all_objs.items()]
            print(l)

    def do_update(self, line):
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
            setattr(all_objs[k], args[2], args[3])
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