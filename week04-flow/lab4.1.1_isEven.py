# lab4.1.1_isEven.py
# Program that asks the user to input an integer and outputs if the number is even or odd.
# This program uses a while loop to keep prompting the user to enter a number until they enter -1.
# author: Niamh Hogan

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


# Source: https://chatgpt.com/c/67be1f94-13b8-8011-8891-6d2ed19b7d60
while True:
    num = int(input("Enter an integer: "))
    if num == -1:
        break