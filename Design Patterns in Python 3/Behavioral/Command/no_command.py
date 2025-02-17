from .abs_command import AbstractCommand

class NoCommand(AbstractCommand):

    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print(f"No command named {self._command}")