from .abs_command import AbstractCommand
from .abs_command_props import AbstractCommandProperties

class CreateOrder(AbstractCommand, AbstractCommandProperties):
    name = "Create order"
    description = "Create a new order"

    def execute(self):
        print("Creating new order... Done")
        # raise NotImplementedError