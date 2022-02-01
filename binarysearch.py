#!/usr/bin/env python3

import random

print("Binary Search\n Enter 'x' to exit")  # header

random_numbers = []

for i in range(1, 10):
    new = random.randint(1, 100)
    random_numbers.append(new)
    
random_numbers = sorted(random_numbers)  #generates a sorted list of random numbers

def main():
    check = input("Enter a number from 1 to 100: ")

    if check == 'x':
        print("Goodbye")
    else:
        check = int(check)
        binary(random_numbers, 0, len(random_numbers)-1, check)
        main()  #gets user input and sends it to the function

def binary(index, low, high, x):
    
    if high >= low:
        mid = (high + low) // 2
        if index[mid] == x:
            print(str(x) + " is in the random numbers\n")

        elif index[mid] > x:
            return binary(index, low, mid-1, x)
        else:
            return binary(index, mid+1, high, x)
    else:
        print(str(x) + " is not in the random numbers\n")  #determines if it's in the pile or not
                      
                  
    
    
main()
