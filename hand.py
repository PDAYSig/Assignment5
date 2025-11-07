'''
This file contains the Hand class. It is used to keep track of which cards are in the hand.
It has a public constant NUMBER_OF_CARDS that determines how many cards the hand can hold.
It only has one method, add_card, that takes a card and adds it to the hand.
'''


from card import Card
class Hand:
    NUMBER_OF_CARDS = 13

    def __init__(self):
        self.cards = []

    def __str__(self):
        show_hand = ""
        for card in self.cards:
            # We create the hand string 
            show_hand = show_hand + f"{card.__str__() :>3}" + " "

        # We want to return "Empty" if the hand has no cards
        if self.cards == None:
            show_hand = "Empty"

        return show_hand
    
    def add_card(self, card) -> None:
        '''This function adds a Card object to the hand'''
        if len(self.cards) < Hand.NUMBER_OF_CARDS:
            self.cards.append(card)
