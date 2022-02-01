#!/usr/bin/env python3

print("Rectangle Thangy")

def repeat():
    check = input("Continue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it

class rectangle:
    
    def perimeter(x, y):
        perimeter = 2*(x+y)
        return perimeter
    
    def area(x, y):
        area = x*y
        return area

    def __init__(self, height, width):
        self.height = height
        self.width = width  #rectangle class with callable methods


def main():
    height = int(input("Input height: "))
    width = int(input("Input width: "))

    p = rectangle.perimeter(height, width)
    a = rectangle.area(height, width)
    print("The perimeter is " + str(p) + "\nThe area is " + str(a))
    repeat()  #gets users input and calculates the stuff

main() 
