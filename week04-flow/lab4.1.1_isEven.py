# lab4.1.1_isEven.py
# Program that asks the user to input an integer and outputs if the number is even or odd.
# author: Niamh Hogan

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")