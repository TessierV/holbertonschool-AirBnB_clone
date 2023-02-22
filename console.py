#!/usr/bin/python3
"""The console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interprete"""
    prompt = '(hbnb) '

    Dict = [
        "BaseModel",
        "User",
        "City",
        "Place",
        "Review",
        "State",
        "Amenity"
        ]


    def do_EOF(self, line):
        """command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create a new instances """
        arg = line.split(" ")
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] != self.Dict:
                print("** class doesn\'t exist **")
            else:
                new_inst = BaseModel()
                new_inst.save()
                print(new_inst.id)

    def do_show(self, line):
        """Print instances"""
        arg = line.split(" ")
        if arg[0] == "":
            print('** class name missing **')
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            if arg[0] == self.Dict:
                try:
                    storage_all = storage.all()
                    obj = arg[0] + "." + arg[1]
                    instance = storage_all[f"{obj}"]
                    print(instance)
                except KeyError:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_destroy(self, line):
        """Deletes an instance"""
        arg = line.split(" ")
        print(arg)
        if arg[0] == "":
            print("** class name missing **")
        else:
            if arg[0] != self.Dict:
                print("** class doesn\'t exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                obj = arg[0] + "." + arg[1]
                if obj in all_objs.keys():
                    del all_objs[obj]
                    storage.save()
                else:
                    print(obj)
                    print("** no instance found **")

    def do_all(self, line):
        """Print all instances"""
        arg = line.split(" ")
        list = []
        storage_all = storage.all()
        if arg[0] == "":
            print(storage_all)
        else:
            try:
                eval(arg[0])
                for obj in storage_all:
                    key = obj.split('.')
                    if key[0] == arg[0]:
                        list.append(str(storage_all[obj]))
                print(list)
            except NameError:
                print('** class doesn\'t exist **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()