# grade.py
# This program reads an input prints out a grade depending on the value
# Author: Alan Healy
# Date Created: 20-FEB-2021

percentage = float(input("Enter the percentage: "))

if (percentage < 0) or (percentage > 100):
    # use ValueError instead
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # so between 0 and 40
    print ("Fail")
elif percentage < 50: # between 40 and 49. if it is already less than 40, above statement will catch it
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit 1")
elif percentage < 70: # between 60 and 69
    print ("Merit 2")
else: # number can now only be between 70 and 100
    print ("Distinction")