#hangman in python

import random

# It's a good practice to name constants in all caps.
WORDS = ("apple", "orange", "banana", "coconut", "pineapple")

# I've adjusted the art slightly for better alignment and clarity.
HANGMAN_ART = {
    0: (
        "  ",
        "  ",
        "  ",
    ),
    1: (
        " o ",
        "   ",
        "   ",
    ),
    2: (
        " o ",
        " | ",
        "   ",
    ),
    3: (
        " o ",
        "/| ",
        "   ",
    ),
    4: (
        " o ",
        "/|\\",
        "   ",
    ),
    5: (
        " o ",
        "/|\\",
        "/  ",
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\",
    )
}

def display_hangman(wrong_guesses):
    """Prints the current state of the hangman."""
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)

def display_board(hint, guessed_letters):
    """Displays the word hint and the letters already guessed."""
    print("\n" + " ".join(hint))
    # It's helpful to show the user which letters they've already tried.
    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 25)

def main():
    answer = random.choice(WORDS)
    # A list of characters is easier to modify than a list with one long string.
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    game_over = False
    max_wrong_guesses = len(HANGMAN_ART) - 1

    print("--- Welcome to Hangman! ---")

    while not game_over:
        display_hangman(wrong_guesses)
        display_board(hint, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1

        if "_" not in hint:
            game_over = True
            print("\nCongratulations! You guessed the word!")
        elif wrong_guesses >= max_wrong_guesses:
            game_over = True
            display_hangman(wrong_guesses)
            print("\nGame Over! You've been hanged.")

    print(f"The word was: {answer}")

if __name__ == "__main__":
    main()
