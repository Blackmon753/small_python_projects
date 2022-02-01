#!/usr/bin/env python3

import random

print("Card Dealer")

def main():
    deck = Deck()
    deck.shuffle()
    print("The deck has been shuffled.")

    count = int(input("How many cards would you like?: "))  #asks the user how many cards they want

    for x in range(count):
        deck.draw().show()  #draws the cards
        
        
    print("\nThere are " + str(deck.remaining()) + " cards left in the deck.")     #prints out the size of the deck


class Cards():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))  #creates the card object


class Deck():
    def __init__(self):
        self.cards = []
        self.build()  

    def build(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        ranks = [ "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace" ]
        for suit in suits:
            for value in ranks:
                self.cards.append(Cards(value,suit))  #builds the deck

    def show(self):
        for card in self.cards:
            card.show()  #shows the card that was drawn

    def shuffle(self):
            random.shuffle(self.cards)
            return self  #shuffles the cards
        
    def draw(self):
        return self.cards.pop()  #draws a card and removes it from the list

    def remaining(self):
        x = len(self.cards)  #gets the remaining cards in the deck

        return x


main()



