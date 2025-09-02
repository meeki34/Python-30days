import random 

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1 # Only count valid guesses

        if guess == answer:
            print(f"Congratulations! You guessed the number in {guesses} guesses!")
            is_running = False
        elif guess < answer:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    except ValueError:
        print("That's not a valid number. Please try again.")
