# evens.py
# This program prints out even numbers in a range
# Author: Alan Healy
# Date Created: 27-FEB-2021

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong!")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)
