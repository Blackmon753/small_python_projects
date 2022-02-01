#!/usr/bin/env python3

import csv  

print("Customer Viewer")



class customer():
    def __init__(self, id, f_name, l_name, company, address, city, state, zip):
        pass  


def main():
    with open("customers.csv", "r") as customers:
        
        csvFileArray = []
        for row in csv.reader(customers, delimiter = ','):
            csvFileArray.append(row)
        print(csvFileArray[1])  #I honestly give up with this crap. Its too late. The other projects work just fine. 
         

def repeat():
    check = input("Continue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it
main()
