# guess2.py
# This program lets the user guess a number, and tells them if they are too
# high or low
# Author: Alan Healy
# Date Created: 27-FEB-2021

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:  # number cant be equal or too low, so it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)