import abc

class AbstractState(abc.ABC):

    def __init__(self, context):
        self._cart = context

    @abc.abstractmethod
    def add_item(self):
        pass

    @abc.abstractmethod
    def remove_item(self):
        pass

    @abc.abstractmethod
    def empty_cart(self):
        pass

    @abc.abstractmethod
    def checkout(self):
        pass

    @abc.abstractmethod
    def pay(self):
        pass