from abs_observer import AbstractObserver
import abc

class AbstractSuject(abc.ABC):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbstractObserver):
            raise ValueError("Observer is not derived from AbsObserver")
        self._observers.add(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except KeyError:
            print("Observer not found")

    def notify(self, value=None):
        for observer in self._observers:
            if value==None:
                observer.update()
            else:
                observer.update()
            
