#!/usr/bin/env python3
""" This is the creation of the console"""

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

    def do_emptyline(self):
        """ Handles emptylines"""

        pass

    def do_create(self, args):
        """Creates an instance of BaseModel"""

        if not (args):
            print("** class name missing **")

        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id."""

        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in classes:
                print("** class doesn't exist **")

            else:
                for key, value in storage.all().items():
                    if args[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
        and id (save the change into the JSON file)."""

        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args < 2):
            print("** instance id missing **")
            return
        if ags[0] not in classes:
            print("** class doesn't exist **")
            return

        for key, value in storage.all().items():
            if args[1] == value.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

        def do_all(self, args):
            split_args = shlex.split(args)
            n_list = []
            dict_json = models.storage.all()

            if args:
                try:
                    for key in models.storage.all():
                        if split_args[0] == key.split('.')[0]:
                            n_list.append(str(dict_json[key]))
                    print(n_list)
                except Exception:
                    print("** class doesn't exist**")

        def do_update(self, args):
            """ updates an instance """

            args = args.split()
            if len(args) == 0:
                print("** class name missing**")
                return False

            if args[0] in classes:
                if len(args) > 1:
                    key = len(args) + '.' + args[1]
                    if key in storage.all():
                        if len(args) > 2:
                            if len(args) > 3:
                                setattar(storage.all()[key], args[2]. args[3])
                                storage.all()[key].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
