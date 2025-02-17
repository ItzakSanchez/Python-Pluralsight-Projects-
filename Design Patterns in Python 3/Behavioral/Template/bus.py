from abs_transport import AbstractTransport

class Bus(AbstractTransport):

    def start_engine(self):
        print("Starting bus engine")

    def leave_terminal(self):
       print("Leaving bus terminal")

    def travel(self):
        print("Traveling in bus...")

    def entertainment(self):
        print("Looking fields through window")

    def arrive_destination(self):
        print(f"Arriving at {self._destination}")