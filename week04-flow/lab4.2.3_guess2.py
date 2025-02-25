# lab4.2.3_guess2.py
# This program tells the user if they are too high or too low and keeps prompting the user to guess the number until they guess correctly.
# author: Niamh Hogan

numberToGuess = 14

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess > numberToGuess:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess, sep=" ")


# # Extra: This program generates a random number between 0 and 100 and asks the user to guess the number.
import random

ranNum = random.randint(0, 100)

guess = int(input("Please guess the number: "))
while guess != ranNum:
    if guess > ranNum:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", ranNum, sep=" ")
