# importanting Player class and random library
import random
from player import Player

# creating Game class
class Game:
    def __init__(self):
        self.players = [Player(), Player(), Player()]
        self.guess = 0  # initialized to 0 initially