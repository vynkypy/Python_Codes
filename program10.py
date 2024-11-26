# Guess the Number

# A game where the user tries to guess a random number within a range.


import random

number = random.randint(1, 100)

attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break