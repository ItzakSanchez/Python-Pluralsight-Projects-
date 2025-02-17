from pickle import dumps, loads

class Memento:

    def set_state(self, game_state):
        self.game_state = dumps(game_state)

    def get_state(self):
        return loads(self.game_state)

    