# week04Extra.py
# This program does the Extra Q's from Lab 4.1
# Author: Alan Healy
# Date Created: 20-FEB-2021

# Q.3
# "69.5 gets rounded to 70". Assuming number ares rounded to nearest integer
# e.g. 69.4 = 69, but 69.5 = 70

# use the round funtion
#percentage = round(float(input("Enter the percentage: ")))

#print (percentage)

# carry on with usual if statements in "grade.py"
# 

# Q.4
# "keep prompting user until they enter -1"

number = int(input("Enter an integer (enter -1 to quit): "))

while number != (-1):
    if (number % 2) == 0:
        print("{} is an even number.".format(number))
        # prompt for number to stop endless loop
        number = int(input("Enter an integer (enter -1 to quit): "))
    else:
        print("{} is an odd number.".format(number))
        # prompt for number
        number = int(input("Enter an integer (enter -1 to quit): "))
else:
    print("-1 entered. Now exiting the program.")
