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

        self.display_winner()

    def display_winner(self):
        highest_score = -1
        winner = 0
        player_number = 1

        for player in self.game.players:
            print("[Application] Player " + str(player_number) + " final score: " + str(player.score))
            
            if player.score > highest_score:
                highest_score = player.score
                winner = player_number
            
            player_number += 1

        print("\n[Application] Winner is Player " + str(winner) + " with a score of " + str(highest_score))


# executing program from Entry Point
if __name__ == "__main__":
    app = Application()
    app.run_game()