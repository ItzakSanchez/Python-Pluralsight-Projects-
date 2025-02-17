import abc

class AbstractStrategy(abc.ABC):

    @abc.abstractmethod
    def calculate(self, order):
        pass