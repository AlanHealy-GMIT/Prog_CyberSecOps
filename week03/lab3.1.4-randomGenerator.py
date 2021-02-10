# randomGenerator.py
# This program prints out a random number between 1 and 10
# Author: Alan Healy
# Date Created: 10-FEB-2021

# import the "random" library

import random

# ask user to enter two numbers for a range
x = int(input("Enter first number in range: "))
y = int(input("Enter last number in range: "))

number = random.randint(x, y)
print("A random number between {} and {} is: {}".format(x, y, number))
