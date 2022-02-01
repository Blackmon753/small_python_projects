#!/usr/bin/env python3

print("Customer/Employee Data Entry")

def repeat():
    check = input("\nContinue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it

class person():
    def __init__(self, f_name, l_name, email,):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

class customer(person):
    def __init__(self, f_name, l_name, email, customer_number):
       person.__init__(self, f_name, l_name, email)
       self.customer_number = customer_number

    def __str__(self):
        return "First Name: %s \nLast Name: %s \nEmail: %s \nNumber: %s" % (self.f_name, self.l_name, self.email, self.customer_number)
    

class employee(person):
    def __init__(self, f_name, l_name, email, ss_number):
       person.__init__(self, f_name, l_name, email)
       self.ss_number = ss_number
       

    def __str__(self):
        return "First Name: %s \nLast Name: %s \nEmail: %s \nSSN: %s" % (self.f_name, self.l_name, self.email, self.ss_number)

def main():
    choice = input("Customer or employee? (c/e): ")

    if choice == "c":
        print("Data Entry")
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        email = input("Email: ")
        number = input("Number: ")

        c1 = customer(f_name, l_name, email, number)

        print("\nCUSTOMER")
        print(c1)
    elif choice == "e":
        print("Data Entry")
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        email = input("Email: ")
        number = input("SSN: ")

        e1 = employee(f_name, l_name, email, number)

        print("\nEMPLOYEE")
        print(e1)
    else:
        print("C'mon man.  Put a valid answer in")
        main()
    repeat()
    
main()
