import random

stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

word_list = ["apple", "banana", "grape", "mango", "pineapple", "orange"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = ["_"] * word_length
end_of_game = False

print("Welcome to Hangman!")
print("Word to guess: " + " ".join(display))

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}. Try another letter.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose! The word was:", chosen_word)


    print("Word to guess: " + " ".join(display))
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win! ")
