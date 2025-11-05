import random
from card import Card
'''
This file contains the Deck class. It is used to keep track of which cards are in the deck
as well as shuffling and dealing the cards.
'''


class Deck:
    def __init__(self):
        self.__card_count = 52
        self.deck = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['H', 'S', 'D', 'C']
        start_deck = {
                    'H' : ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], 
                    'S' : ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], 
                    'D' : ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], 
                    'C' : ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
        }
        # we add the cards to our deck variable as a Card type
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle(self):
        '''This function is used to shuffle the cards'''
        random.shuffle(self.deck)

    def deal(self):
        '''This function deals a single card from the deck'''
        self.__card_count -= 1
        return self.deck.pop()

    def __str__(self):
        deck_str = ""
        card_count = 0
        for card in self.deck:
            #we check if the card count is a multiple of 13
            card = str(card)
            if card_count % 13 == 0 and card_count != 0 and card_count != len(self.deck):
                deck_str = deck_str + '\n' + card.rjust(3) + ' '
            elif card_count == 0:
                deck_str = card.rjust(3) + ' '
            elif card_count == len(self.deck):
                deck_str = deck_str + card.rjust(3)
            else:
                deck_str = deck_str + card.rjust(3) + ' '
            
            card_count += 1

        return deck_str
    
deck = Deck()
print(deck)
deck.shuffle()
print(deck)

deck.deal()
print(deck)