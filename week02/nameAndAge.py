# nameAndAge.py
# This program reads in a name and age and outputs it
# Author: Alan Healy
# Date Created: 31-JAN-2021

# reads user inputted values and assigns them to variables
name = input("Please enter your name: ")
age = int(input("Please enter your age: ")) # converts str to int

# output values to user
#print("Hello {}, your age is {}.".format(name,age))

# same as above but modified to include tab at end of name
print("Hello {},\t your age is {}.".format(name,age))
