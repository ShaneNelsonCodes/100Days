import random
from Day12_Guess_The_Number_Art import logo

easy_levels = 10
hard_levels = 5

def check_answer(guess, answer, lives):
    if guess > answer:
        print("Too high")
        return lives - 1
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return easy_levels
    else:
        return hard_levels


def play_game():
    play_again = 'y'
    while play_again == 'y':
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        lives = set_difficulty()

        answer = random.randint(1, 100)

        guess = 0
        while guess != answer:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            lives = check_answer(guess=guess, answer=answer, lives=lives)
            if lives == 0:
                print("You've run out of guesses, you lose")
                break
            elif guess != answer:
                print("Guess again.")
        play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no. ")
play_game()