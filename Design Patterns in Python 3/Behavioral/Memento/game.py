from pickle import dumps, loads
from dataclasses import dataclass
from memento import Memento

@dataclass
class GameState:
    name: str
    level: int

class Game:

    def __init__(self, name):
        self.game_state = GameState(name, 1)
    
    def create_memento(self):
        memento = Memento()
        memento.set_state(self.game_state)
        return memento
    
    def load_memento(self, memento):
        self.game_state = memento.get_state()