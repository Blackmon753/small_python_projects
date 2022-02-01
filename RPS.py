#!/usr/bin/env python3

import random

print("Rock Paper Scissors")

global name
name = input("What is your name?: ")

def repeat():
    check = input("Continue (y/n) : ")

    if check.lower() == "y":
        main()
    elif check.lower() == "n":
        print("Fine then")
    else:
        print("C'mon man.  Put a valid answer in")
        repeat()  #repeats if the user wants it

class player():
    def __init__(self, name, r_value):
        self.name = name
        self.r_value = r_value  #player superclass


class bart(player):

    def RPS():
        r_value = "Rock"
        return r_value

    def name():
        name = "Bart"
        return name

class lisa(player):

    def RPS():
        choice = ["Rock", "Paper", "Scissors"]
        return random.choice(choice)

    def name():
        name = "Lisa"
        return name  #classes for bart and lisa
    
def main():

    versus = input("Would you like to play against Bart or Lisa? (b/l): ")

    if versus == "b":
        npc = bart.name()
        npc_c = bart.RPS()
    elif versus == "l":
        npc = lisa.name()
        npc_c = lisa.RPS()
    else:
        print("C'mon man.  Put a valid answer in")
        main()  #lets the player choose the opponent

    initial = input("Rock, paper, or scissors? (r/p/s): ")

    if initial == "r":
        choice = "Rock"
    elif initial == "p":
        choice = "Paper"
    elif initial == "s":
        choice == "Scissors"  #converts the user input to something easier to mess with 
    
    if choice == npc_c:
        print("Draw!")
    elif choice == "Rock" and npc_c == "Paper":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + npc + " wins!")
    elif choice == "Rock" and npc_c == "Scissors":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + name + " wins!")
    elif choice == "Paper" and npc_c == "Scissors":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + npc + " wins!")
    elif choice == "Paper" and npc_c == "Rock":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + name + " wins!")
    elif choice == "Scissors" and npc_c == "Rock":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + npc + " wins!")
    elif choice == "Scissors" and npc_c == "Paper":
        print(name + ": " + choice + "\n" + npc + ": " + npc_c + "\n" + name + " wins!")  #game logic

    repeat()
 

main()

        
