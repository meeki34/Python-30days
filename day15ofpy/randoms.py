import random

low = 1
high = 100 
guesses = 0 
number = random.randint(low,high)

while True:
    guesses += 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    if guess > number:
        print("Too high")
        high = guess
    elif guess < number:
        print("Too low")
        low = guess
    else:
        print(f"Correct! The number was {number}")
        break
print(f"It took you {guesses} guesses")