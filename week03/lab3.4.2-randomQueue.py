# randomQueue.py
# This program puts random numbers in a queue
# Author: Alan Healy
# Date Created: 13-FEB-2021

# import the "random" library
import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print("Queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print("The current number is {} and the queue is {} ".format(
        currentNumber, queue))

print("The queue is now empty.")
