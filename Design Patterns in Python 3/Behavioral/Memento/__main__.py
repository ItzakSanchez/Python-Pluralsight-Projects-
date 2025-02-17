from game import Game
from memento import Memento
import random


game = Game("Slayer1")
game.game_state.level = 20
print (f"Game {game.game_state.name}: lvl.{game.game_state.level}")
memento = game.create_memento()
game.game_state.level = 35
print (f"Game {game.game_state.name}: lvl.{game.game_state.level}")
print("*Restoring state*")
game.load_memento(memento)
print (f"Game {game.game_state.name}: lvl.{game.game_state.level}")
