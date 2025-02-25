# lab4.2.4_average.py
# This program reads in numbers until the user enters 0 and then it will output the average of the numbers entered.
# author: Niamh Hogan

numbers = []

number = int(input("Enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}.")