#!/usr/bin/python3
"""The console"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        "command to exit the program""
        return True

    def emptyline(self):
        pass

    def do_quit(self, line):
        "Quit command to exit the program"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
