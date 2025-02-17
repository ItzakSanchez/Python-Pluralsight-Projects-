from abs_state import AbstractState

class EmptyState(AbstractState):
    
    def add_item(self):
        self._cart.items += 1
        print(f"Added 1 item to cart. Total items:{self._cart.items}")
        self._cart.state = self._cart.not_empty_state
        print(f"Cart items:{self._cart.items}")
        print(f"Cart state:{self._cart.state}")

    def remove_item(self):
        print(f"Cart is already empty")

    def empty_cart(self):
        print(f"Cart is already empty")

    def checkout(self):
        print(f"Cannot checkout, cart is empty")

    def pay(self):
        print(f"Cannot pay, cart is empty")
