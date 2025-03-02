# lab5.1.3_randNums.py
# This program generates 10 random numbers & puts them into a list.
# The program then prints out the numbers in the list.
# Following this, the program prints out a number from the list & removes it with the current numbers remaining in the queue.
# This continues until the queue is empty.
# author: Niamh Hogan

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print (f"queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print (f"current Number is {currentNumber}, and the queue is {queue}")

print ("The queue is now empty.")