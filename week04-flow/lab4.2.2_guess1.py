# lab4.2.2_guess1.py
# This program asks the user to guess the number.
# author: Niamh Hogan

numberToGuess = 50

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong!")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess, sep=" ")