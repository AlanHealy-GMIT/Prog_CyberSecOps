# sub.py
# This program subtracts a number from another
# Author: Alan Healy
# Date Created: 10-FEB-2021

# user inputs a number which is a string. this has to be converted to an int
# in order to perform calculations on it

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

answer = x - y

print("{} minus {} is {}.".format(x, y, answer))
