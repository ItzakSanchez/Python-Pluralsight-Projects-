from abs_state import AbstractState

class NotEmptyState(AbstractState):

      
    def add_item(self):
        self._cart.items += 1
        print(f"Added 1 item to cart. Total items:{self._cart.items}")
        self._cart.state = self._cart.not_empty_state
        print(f"Cart items:{self._cart.items}")
        print(f"Cart state:{self._cart.state}")

    def remove_item(self):
        self._cart.items -= 1
        print(f"Removed 1 item to cart. Total items:{self._cart.items}")
        if self._cart.items < 1:
            self._cart.state = self._cart.empty_state
        print(f"Cart items:{self._cart.items}")
        print(f"Cart state:{self._cart.state}")

    def empty_cart(self):
        self._cart.items = 0
        self._cart.state = self._cart.empty_state
        print(f"Removing all items. Total items:{self._cart.items}")
        print(f"Cart items:{self._cart.items}")
        print(f"Cart state:{self._cart.state}")

    def checkout(self):
        print(f"Doing checkout... Ready to pay")
        self._cart.state = self.checkout_state

    def pay(self):
        print(f"You have to do checkout to Pay")
