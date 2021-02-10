# div.py
# This program divides one number by another
# Author: Alan Healy
# Date Created: 10-FEB-2021

# user inputs a number which is a string. this has to be converted to an int
# in order to perform calculations on it

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x // y)  # // gives the int division
remainder = x % y    # % gives the remainder

print("{} divided by {} is {} with a remainder of {}.".format(
    x, y, answer, remainder))
