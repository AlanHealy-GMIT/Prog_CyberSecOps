# testRegex.py
# This program is for testing Lab 07 regex examples
# Author: Alan Healy
# Date Created: 14-MAR-2021

import re

#regex = "\[.*\]" # dates and time
#regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # IP addresses
regex = "[a-z]+://www.\w{1,64}\.[a-z]{1,10}" #top level domains
filename = "./smallerAccess.txt"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList) != 0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
            #strip the [] from beginning and end
            #print(foundText[1:-1])

