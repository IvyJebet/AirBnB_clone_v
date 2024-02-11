#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Class console"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Command that quits the program"""
        return True

    def help_quit(self, arg):
        """Command that helps quit the program"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Command that signals exit of the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
