# lab4.1.2_grade.py
# This program reads in a students percentage and prints out the corresponding grade.
# Extra: This program rounds up the users input to the nearest whole number to determine the grade.
# author: Niamh Hogan

percentage = float(input("Enter the percentage: "))
# Source: https://www.w3schools.com/python/ref_func_round.asp 
rounded_percentage = round(percentage)

if rounded_percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif rounded_percentage < 40:
    print("Fail")
elif rounded_percentage < 50:
    print("Pass")
elif rounded_percentage < 60:
    print("Merit1")
elif rounded_percentage < 70:
    print("Merit2")
else:
    print("Distinction")