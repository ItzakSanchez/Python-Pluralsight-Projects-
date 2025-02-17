import abc

class AbstractCommand(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass