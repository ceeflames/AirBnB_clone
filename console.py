#!/usr/bin/python3
"""Define the HBNB console."""


import cmd
from models import storage
from shlex import split
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommnad class that defines the command interpreter.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel"}

    def do_create(self, arg):
        try:
            """Create a new instance of BaseModel"""
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwards[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quite command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program"""
        print("")
        return True

    def emptyline(self):
        "An empty line + Enter shouldn't execute anything"
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError
            NameError
            IndexError
            KeyError
        """
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances 
        based or not on the class name.
        """
        args = arg.split(" ")
        if not args:
            all_instances = storage.all().values()
            print([str(instance) for instance in all_instances])
        else:
            class_name = args[0]
            if class_name in self.__classes:
                class_instances = storage.all(class_name).values()
                print([str(instance) for instance in class_instances])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance by updating attribute."""
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** sttribute name missing **")
        except ValueError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
