from state_empty import EmptyState
from state_not_empty import NotEmptyState
from state_check_out import CheckoutState
from state_paid_for import PaidState

class ShoppingCart:

    def __init__(self):
        self.empty_state = EmptyState(self)
        self.not_empty_state = NotEmptyState(self)
        self.checkout_state = CheckoutState(self)
        self.paid_state = PaidState(self)

        self.items = 0
        self.state = self.empty_state

    # @property
    # def items(self):
    #     return self._items
    
    # @property
    # def state(self):
    #     return self._state

    def add_item(self):
        self.state.add_item()

    def remove_item(self):
        self.state.remove_item()
    
    def empty_cart(self):
        self.state.empty_cart()

    def checkout(self):
        self.state.cheeckout()

    def pay(self):
        self.state.pay()
