# isEven.py
# This program checks if a number is odd or even.
# Author: Alan Healy
# Date Created: 20-FEB-2021

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))


