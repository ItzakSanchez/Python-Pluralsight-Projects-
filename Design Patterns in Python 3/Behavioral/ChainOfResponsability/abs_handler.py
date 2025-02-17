import abc

class AbstractHandler(abc.ABC):

    @property
    @abc.abstractmethod
    def successor(self):
        pass

    @abc.abstractmethod
    def handle(self, request):
        pass