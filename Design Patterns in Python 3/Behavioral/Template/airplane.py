from abs_transport import AbstractTransport

class Airplane(AbstractTransport):

    def start_engine(self):
        print("Starting airplane engine")

    def leave_terminal(self):
       print("Leaving airport terminal")

    def travel(self):
        print("Traveling in airplane...")

    def entertainment(self):
        print("Looking clounds through window")

    def arrive_destination(self):
        print(f"Arriving at {self._destination}")