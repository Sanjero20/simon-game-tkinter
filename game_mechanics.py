# SIMON Game (Short-Term Memory Skill Game)
# Game Mechanics

# Note this code does not have any error handling

import os
import time
import random

class Game:
    def __init__(self):
        self.game_running = False
        self.numbers = []

    def game_secquence(self):
        self.start()
        while self.game_running:
            self.add()
            self.show_numbers()
            self.guess()

    def add(self):
        """Append a random number into the self.numbers """
        self.numbers.append(random.randint(0, 9))

    def show_numbers(self):
        """Show the current numbers in the list"""
        self.seq = "".join([str(x) for x in self.numbers])
        # Hide the numbers within 3 seconds
        counter = 3
        for i in range(4):
            print(f"Memorize: '{self.seq}'")
            print(f"\n-- Hiding in {counter} --")
            time.sleep(1)
            counter -= 1
            os.system("cls")
            
        os.system("cls")

    def guess(self):
        """Gets the player input"""
        hidden = "".join(["*" for i in range(len(self.seq))])
        print("Hidden:", hidden)
        p_answer = input(" Guess: ")
        self.verify(p_answer)

    def verify(self, player_input):
        """Check if the player input is the same with the numbers"""
        player = [int(x) for x in player_input]
        if player != self.numbers:
            print("\n-- You lost --")
            print(f"Secquence:   {self.numbers}")
            print(f"Your Answer: {player}")
            self.game_running = False
        else:
            print("\n-- Correct --")
            time.sleep(1)
            os.system("cls")

    def start(self):
        g = input("Play Game(y/n): ")
        if g == "y":
            self.game_running = True
            os.system("cls")

game = Game()
game.game_secquence()