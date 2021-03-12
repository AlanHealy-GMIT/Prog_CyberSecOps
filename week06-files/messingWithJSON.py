# quiz.py
# This program is for testing Lab 06 JSON examples
# Author: Alan Healy
# Date Created: 12-MAR-2021

import json

filename = "testDict.json"

# sample = dict(name = 'fred', age = 31, grades = [1,34,55])

# def writeDict(obj):
#     with open(filename, 'wt') as f:
#         json.dump(obj,f)

# # test function
# writeDict(sample)

def readDict():
    # will throw error if file does not exist
    with open(filename) as f:
        return json.load(f)

# test function
somedict = readDict()
print(somedict)