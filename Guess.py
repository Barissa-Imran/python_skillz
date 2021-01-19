# ask the user for input
# check to see if the input is the guess
# if true then congratulate
# if not the user keeps guessing

import random
guess = int(input("Guess any number between 1-10: "))
num = random.randrange(1, 10)


def guessing(guess):
    while True:
        if guess == num:
            print(f"correct, {guess} is the right answer")
            break
        elif guess < num:
            print("Your guess is lower than the number")
            guess = int(input("guess again: "))
            continue
        elif guess > num:
            print("your guess is greater than the number")
            guess = int(input("guess again: "))
            continue

guessing(guess)
