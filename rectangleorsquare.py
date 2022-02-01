#!/usr/bin/env python3

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

class square(rectangle):

    def __init__(self, length):
        self.length = length
        
    def perimeter(x):
        perimeter = 4*(x)
        return perimeter

    def area(x):
        area = x*x
        return area  #square class inheriting from the rectangle class

def main():
    choice = input("Rectangle or square? (r/s): ")

    if choice == "r":
        height = int(input("Input height: "))
        width = int(input("Input width: "))

        p = rectangle.perimeter(height, width)
        a = rectangle.area(height, width)
        print("The perimeter is " + str(p) + "\nThe area is " + str(a))
        repeat()  #gets users input and calculates the stuff

    elif choice == "s":
        length = int(input("Input length of sides: "))

        p = square.perimeter(length)
        a = square.area(length)
        print("The perimeter is " + str(p) + "\nThe area is " + str(a))
        repeat()  #does the same but for a square

    else:
        print("C'mon man.  Put a valid answer in")
        main()
main() 
    
