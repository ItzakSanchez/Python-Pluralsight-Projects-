import abc

class AbstractCommandProperties(abc.ABC):
    
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def description(self):
        pass