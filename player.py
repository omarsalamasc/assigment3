# importing random library
import random

# creating player class
class Player:
    def __init__(self):
        # Player starts with score 0
        self.score = 0  

    def roll(self):
        # using dice roll ( from 1-6)
        return random.randint(1, 6)
    