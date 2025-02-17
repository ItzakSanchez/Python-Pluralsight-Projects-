from .abs_command import AbstractCommand
from .abs_command_props import AbstractCommandProperties

class UpdateOrder(AbstractCommand, AbstractCommandProperties):
    name = "Update Order"
    description = "Update an order's quantity of products"

    def __init__(self, args):
        self._new_quantity = args[1]
    
    def execute(self):
        old_quantity = 2
        #Simulate database update
        print("Updating database...")

        #Simulate logging the update
        print(f"Logging: Value updated from '{old_quantity}' to '{self._new_quantity}'")