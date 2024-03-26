#!/usr/bin/env python3
"""
Console for AirBnB clone
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import json
import shlex


def first_pass(arg):
    """
    returns upon invalid arg value
    """
    if not arg:
        print("** class name missing **")
        return


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def_class = [
            'BaseModel', 'User',
            'City', 'State', 'Place',
            'Review', 'Amenity']

    meth = ['create', 'destroy', 'update', 'show', 'all', 'count']

    def precmd(self, arg):
        """
        This parses the console input
        """
        if '.' in arg and '(' in arg and ')' in arg:
            dC = arg.split('.')
            dM = dC[1].split('(')
            param = dM[1].split(')')
            if dC[0] in HBNBCommand.def_class and dM[0] in HBNBCommand.meth:
                arg = dM[0] + ' ' + dC[0] + ' ' + param[0]
        return arg

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        else:
            n_dict = {
                    'BaseModel': BaseModel,
                    'User': User, 'State': State,
                    'City': City, 'Review': Review,
                    'Place': Place, 'Amenity': Amenity}
            my_model = n_dict[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        first_pass(arg)
        spl_arg = arg.split(' ')

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        elif len(spl_arg) == 1:
            print("** instance id missing **")
        else:
            obj_tot = storage.all()
            for key, value in obj_tot.items():
                name_obj = value.__class__.__name__
                id_obj = value.id
                if name_obj == spl_arg[0] and id_obj == spl_arg[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Change is saved into the JSON file
        """
        first_pass(arg)
        spl_arg = arg.split(' ')

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        elif len(spl_arg) == 1:
            print("** instance id missing **")
        else:
            obj_tot = storage.all()
            for key, value in obj_tot.items():
                name_obj = value.__class__.__name__
                id_obj = value.id
                if name_obj == spl_arg[0] and id_obj == spl_arg[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        first_pass(arg)
        spl_arg = arg.split(' ')

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        else:
            obj_tot = storage.all()
            inst_list = []
            for key, value in obj_tot.items():
                name_obj = value.__class__.__name__
                if name_obj == spl_arg[0]:
                    inst_list += [value.__str__()]
            print(inst_list)

    def do_count(self, class_name):
        """
        This retrieves the number of instances
        of a class
        """
        count = 0
        obj_tot = storage.all()
        for key, value in obj_tot.items():
            cl_name = key.split('.')
            if cl_name[0] == class_name:
                count = count + 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        Change is saved into JSON file.
        """
        first_pass(arg)
        delim = ""
        for argv in arg.split(','):
            delim = delim + argv

        spl_arg = shlex.split(delim)

        if spl_arg[0] not in HBNBCommand.def_class:
            print("** class doesn't exist **")
        elif len(spl_arg) == 1:
            print("** instance id missing **")
        else:
            obj_tot = storage.all()
            for key, v in obj_tot.items():
                name_obj = v.__class__.__name__
                id_obj = v.id
                if name_obj == spl_arg[0] and id_obj == spl_arg[1].strip('"'):
                    if len(spl_arg) == 2:
                        print("** attribute name missing **")
                    elif len(spl_arg) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, spl_arg[2], spl_arg[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
