# importanting Player class and random library
import random
from player import Player

# creating Game class
class Game:
    def __init__(self):
        self.players = [Player(), Player(), Player()]
        self.guess = 0  # initialized to 0 initially

    def start(self):
        # Set a random guess number between 1 and 6
        self.guess = random.randint(1, 6)
        print("[Game] Guess number for this round is " + str(self.guess))