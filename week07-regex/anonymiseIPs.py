# testRegex.py
# This program is for anonymising IP addresses
# Author: Alan Healy
# Date Created: 14-MAR-2021

import re

regex = "\d{1,3}\.\d{1,3} " # with space at end
replacementText = "xxx.xxx " # again with space
filename = "./smallerAccess.txt"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            newLine = re.sub(regex, replacementText, line)
            # view result
            print(newLine)
            outputFile.write(newLine)