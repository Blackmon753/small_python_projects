#!/usr/bin/env python3

import random

def repeat():
    check = input("\nContinue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it

class randomintlist():
    def __init__(self, count, int_list):
        self.count = count
        self.int_list = self.create(count)
        self.final_count = self.item_count(self.int_list)
        self.total = self.total(self.int_list)
        self.average = self.average(self.int_list, self.total, self.final_count)
              
    def create(self, count):
        int_list = []
        for x in range(count):
            next_int = r_number = random.randint(1, 100)
            int_list.append(next_int)
        return int_list

    def item_count(self, int_list):
        self.int_list
        length = len(int_list)
        return length
    
    def total(self, int_list):
        
        total = sum(int_list)
        return total
    
    def average(self, int_list, total, length):
        average = (total / length)
        return average
    
    
    
    def __str__(self):
        
        return "Integers: %s\nCount: %s\nTotal: %s\nAverage: %s" % (self.int_list, self.final_count, self.total, self.average)

def main():
    int_list = []
    count = int(input("How many integers should the list contain: "))
    new = randomintlist(count, int_list)
    print(new)
    repeat()

    
main() 
