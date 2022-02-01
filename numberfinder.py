#!/usr/bin/env python3

import random
guess_count = 0

print("Numbah Findah\n Enter 'x' to exit")  # header

def main():
    x = int(input("Enter a number from 1 to 100: "))
    finder(1, 100, x, 50)  #gets the numbah from the user

def finder(low, high, x, guess):
    global guess_count
    guess_count+=1
    
    
    if guess == x and guess_count == 1:
        print("Guess " + str(guess_count) + " is " + str(guess) + "\nThe computer got it in 1 guess!")
    elif guess ==x:
        print("Guess " + str(guess_count) + " is " + str(guess) + "\nThe computer found it in " + str(guess_count) + " guesses" )

    elif x < guess:
        newguess = random.randint(low, guess)
        print("Guess " + str(guess_count) + " is " + str(guess))
        finder(low, guess, x, newguess)
        
    elif x > guess:
        newguess = random.randint(guess, high)
        print("Guess " + str(guess_count) + " is " + str(guess))
        finder(guess, high, x, newguess)  #finds da numbah
main()
