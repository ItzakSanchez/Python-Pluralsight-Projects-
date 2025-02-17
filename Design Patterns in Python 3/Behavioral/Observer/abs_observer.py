import abc

class AbstractObserver(abc.ABC):

    @abc.abstractmethod
    def update(self, value):
        pass