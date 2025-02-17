import abc

class AbstractTransport(abc.ABC):

    def __init__(self, destination):
        self._destination = destination

    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel()
        self.arrive_destination()

        

    @abc.abstractmethod
    def start_engine(self):
        pass

    def leave_terminal(self):
        print("Leaving terminal")

    @abc.abstractmethod
    def travel(self):
        pass

    def entertainment(self):
        pass

    def arrive_destination(self):
        print(f"Arriving at {self._destination}")