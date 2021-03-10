# quiz.py
# This program goes through the quiz questions for lab 06
# Author: Alan Healy
# Date Created: 10-MAR-2021


with open("test-b.txt", "w") as f:
    data = f.write("test b\n") #returns number of chars written? yes
    print(data)


with open("test-b.txt", "w") as f2:
    data = f2.write("another line\n")  # open file again
    print(data)
