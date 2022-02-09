#!/usr/bin/env python3

print("Tree Pattern")


def main():
    trees = int(input("Enter the number of branches: "))
    branch(trees)  #takes user input

def branch(x):
    
    add = "*****"
    ast = ""  #variables to make the tree.  
    
    if x == 0:
        return
    
    else:        
        branch(x-1)
        for x in range(1, x+1):
            ast += add
        print(str(x) + " " + ast)
        branch(x-1)  #makes the tree
        
        
main()
