# lab4.2.5_topthree.py
# This program generates 10 random numbers (0-100) and prints them out then prints out the top three.
# author: Niamh Hogan

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

numbers = []

for i in range(0, howMany):
    numbers.append(random.randint(rangeFrom, rangeto))
print(f"{howMany} random numbers\t {numbers}")
# Source: https://www.w3schools.com/python/ref_random_randint.asp

top0nes = numbers.copy()

top0nes.sort(reverse = True)
print(f"Top {topHowMany} are {top0nes[0:topHowMany]}")
# Source: https://www.w3schools.com/python/ref_list_sort.asp