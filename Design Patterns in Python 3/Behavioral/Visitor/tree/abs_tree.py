import abc

class AbstractTree(abc.ABC):

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def accept(self, visitor):
        pass