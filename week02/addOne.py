# addOne.py
# This program reads in a number and adds to it
# Author: Alan Healy
# Date Created: 31-JAN-2021

# Ask user for a number, convert from str to int, and assign to variable "number"
number = int(input("Please enter a number: "))

# New variable that adds 1 to user inputted number
newNumber = number + 1

# Print answer to cmd line
print(str(number) + " + 1 = " + str(newNumber))

# Using 2nd format method for practice
print("{} + 1 = {}".format(number,newNumber))