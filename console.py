#!/usr/bin/python3
""" Command interpreter for the console """
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Airbnb command line interpreter """
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    commands = ["create", "show", "destroy", "update", "all"]

    def precmd(self, line):
        """ Analyzes the whole command before executing """
        if '.' in line and '(' in line and ')' in line:
            arg = line.split('.')
            fur_arg = arg[1].split('(')
            more_arg = fur_arg[1].split(')')
            if arg[0] in self.classes.keys() and fur_arg[0] in self.commands:
                line = fur_arg[0] + ' ' + arg[0] + ' ' + more_arg[0]
        return line

    def default(self, line):
        """ overrided default method """
        self.precmd(line)

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            my_model = self.classes[line]()
            print(my_model.id)
            my_model.save()

    def do_show(self, line):
        """
        prints the string representation of an instance
        Based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) > 0 and args[0] not in self.classes.keys():
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
        elif len(args) > 0 and args[0] not in self.classes.keys():
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
        tribe = line.split(' ')
        if line and line not in self.classes.keys():
            print("** class doesn't exist **")
        elif not line or line in self.classes.keys():
            all_objs = storage.all()
            obj = []
            for i, j in all_objs.items():
                if tribe[0] == j.__class__.__name__:
                    obj.append([j.__str__()])
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
        elif args[0] not in self.classes.keys():
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
