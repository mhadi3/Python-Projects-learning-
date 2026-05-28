import random

logo = "NUMBER GUESSING GAME"

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0

    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0 and guess != answer:
            print("You've run out of guesses. Refresh the page to run again.")


game()
