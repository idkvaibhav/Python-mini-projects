import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def guess_number(self):
        return int(input(f"{self.name}, enter your guess (1-100): "))

def play_guessing_game():
    num_players = int(input("Enter the number of players: "))
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    print("\n=== Number Guessing Game ===\n")
    print("Welcome to the Number Guessing Game!")
    print("You need to guess a number between 1 and 100.")
    print("The player with the fewest attempts to guess the number wins!\n")

    for player in players:
        target_number = random.randint(1, 100)
        print(f"{player.name}, it's your turn to play!")

        game_over = False
        while not game_over:
            guess = player.guess_number()
            player.score += 1

            if guess == target_number:
                game_over = True
                print(f"\nCongratulations, {player.name}! You guessed the number {target_number} in {player.score} attempts!\n")
            elif guess < target_number:
                print("Higher! Try again.\n")
            else:
                print("Lower! Try again.\n")

if __name__ == "__main__":
    play_guessing_game()
