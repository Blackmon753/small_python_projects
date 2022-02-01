#!/usr/bin/env python3

print("Greatest Common Divisor")  #header

def repeat():
    check = input("Continue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it

def main():
    number_1 = int(input("Number 1: "))
    number_2 = int(input("Number 2: "))
    if number_1 < number_2:
        print("Number 2 should be larger than Number 1")
        main()
    else:
        print(calculate(number_1, number_2))  #takes input and checks to ensure it is valid
        repeat()
        
def calculate(x, y):
    if y == 0:
        return x
    else:
        return calculate(y, x%y)  #returns the GCD
main()
