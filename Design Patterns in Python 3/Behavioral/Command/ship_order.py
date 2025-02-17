from .abs_command import AbstractCommand
from .abs_command_props import AbstractCommandProperties

class ShipOrder(AbstractCommand, AbstractCommandProperties):
    name = "Ship Order"
    description = "Ship an order to a client"

    def execute(self):
        return "Shipping order... Done"
        # raise NotImplementedError