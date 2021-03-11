# quiz.py
# This program reads a number from a file
# Author: Alan Healy
# Date Created: 10-MAR-2021

import os.path

filename = "count.txt"

# function to read from file
def readNum():
    try: 
        with open(filename, "rt") as f:
            number = int(f.read())
            return number
    except IOError:
        # error means no file exists, so return 0
        return 0

# function to write to file
def writeNum(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# had to put "if" statement here as it needed to be AFTER the writeNum function
if not os.path.isfile(filename):
    print("File does not exist.")
    # initialise file
    writeNum(0)


num = readNum()
num += 1

print ("We have run this program {} times.".format(num))
writeNum(num)

