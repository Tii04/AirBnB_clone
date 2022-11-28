#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):
    """ Simple command-line processor"""

    prompt = '(hbnb) '
    
    def do_EOF(self, line):
        """ Cleanly exits program"""
        
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
    
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
