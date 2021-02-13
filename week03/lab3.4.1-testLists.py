# testLists.py
# This program tests different types of lists
# Author: Alan Healy
# Date Created: 13-FEB-2021

# demonstrating that lists can have different types
aList = [23, 'hi', True]

# normal
for item in aList:
    print(item)

# print list out in reverse
print('\n'.join(map(str, aList[::-1])))
