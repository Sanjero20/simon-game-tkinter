# Early version of the game mechanics

import random
import os
import time

def guess_game():
    store_numbers.append(random.randint(0, 9))

    print(store_numbers)
    time.sleep(2)

    os.system("cls")

    guess = input("Guess: ")
    verify(guess, store_numbers)

def verify(inpt, lst):
    player_guess = [int(x) for x in inpt]
    print(player_guess)
    print(lst)

    os.system("pause")
    if player_guess == lst:
        pass
    else:
        print("You lose")

# Main Driver
game_running = True
store_numbers = []

play = input("Play Game (y/n): ")
if play == "y":
    os.system("cls")
    while game_running:
        guess_game()


