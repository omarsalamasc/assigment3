# importing game class from game.py
from game import Game

# created class Application
class Application:
    def __init__(self):
        # Create a Game object (being HAS-A relationship)
        self.game = Game()

    # defined run game method with rounds and counting current rounds
    def run_game(self):
        rounds = 5
        current_round = 1

        # creating a while loop to check for rounds 
        while current_round <= rounds:
            print("[Application] Starting Round: " + str(current_round))
            self.game.start()
            self.game.match()
            current_round += 1

