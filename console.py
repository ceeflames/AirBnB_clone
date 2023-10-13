#!/usr/bin/python3
"""Define the HBNB console."""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommnad class that defines the command interpreter.
    """

    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
