from abs_state import AbstractState

class PaidState(AbstractState):
    def add_item(self):
        print(f"Transaction completed, cannot add items")

    def remove_item(self):
        print(f"Transaction completed, cannot remove items")

    def empty_cart(self):
        print(f"Transaction completed, cannot empty cart")

    def checkout(self):
        print(f"Transaction completed, cannot checkout")

    def pay(self):
        print(f"You already paid")