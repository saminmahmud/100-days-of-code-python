# Scope & Number Guessing Game

import random
from art import logo

def guess_the_number():
    print("Welcome to: ")
    print(logo)

    number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100, try to guess it")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5

    is_guess = False
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        if guess_number > number:
            print("Too High.\nGuess again.")
        elif guess_number < number:
            print("Too Low.\nGuess again.")
        else:
            is_guess = True
            print(f"You got it! The answer was {number}")
            break
        guesses -= 1

    if not is_guess:
        print(f"You've run out of guesses, you lose.\nThe answer was {number}.")

    play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit.").lower()
    if play_again == 'y':
        guess_the_number()
    else:
        print("Goodbye.")


guess_the_number()