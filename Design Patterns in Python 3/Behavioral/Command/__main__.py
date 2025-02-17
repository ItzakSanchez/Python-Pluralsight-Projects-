from .create_order import CreateOrder
from .update_order import UpdateOrder
from .ship_order import ShipOrder
from .no_command import NoCommand
import sys
import inspect


def main():
    commands = get_commands()
    if len(sys.argv) <2:
        print_usage(commands)
        exit(1)

    command = parse_command(commands, sys.argv[1:])
    command.execute()
    print("--End of program--")


def get_commands():
    commands = (CreateOrder, UpdateOrder)
    # commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.__name__, cls] for cls in commands)


def print_usage(commands):
    print("Usage: python -m Command <CommandName> [arguments]")
    print("Commands:")
    for command in commands.values():
        print(f"\t{command.__name__}: {command.description}")


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    s = inspect.signature(command)
    return command(args) if len(s.parameters) else command()

main()