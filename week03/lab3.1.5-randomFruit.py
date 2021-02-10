# randomFruit.py
# This program prints out a random fruit from a list
# Author: Alan Healy
# Date Created: 10-FEB-2021

# import the "random" library

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# pick random number between 0 and length of list -1 (as it starts at 0)
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A random fruit is: {}".format(fruit))
