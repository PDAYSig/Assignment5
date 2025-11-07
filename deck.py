'''
Defines the Deck class, used to keep track of which cards are in the deck
as well as shuffling and dealing the cards.
'''

import random
from card import Card

class Deck:
    def __init__(self):
        self.__card_count = 52
        self.deck = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['H', 'S', 'D', 'C']

        # we add the cards to our deck variable as a Card type
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.deck.append(card)

    def shuffle(self):
        '''Used to shuffle the deck'''
        random.shuffle(self.deck)

    def deal(self):
        '''Returns and removes (deals) a single card from the deck'''
        self.__card_count -= 1
        dealt_card = self.deck[0]
        self.deck.remove(dealt_card)
        return dealt_card

    def __str__(self):
        deck_str = ""
        card_count = 0
        for card in self.deck:
            #we check if the card count is a multiple of 13
            card = str(card)

            # We want to print a new line after every 13th card but we must account for the first and last rows
            if card_count % 13 == 0 and card_count != 0 and card_count != len(self.deck):
                deck_str = deck_str + '\n' + card.rjust(3) + ' '
            
            # If we have the first card in the iteration, we can't add it to none and thus we must set deck_str as the card
            elif card_count == 0:
                deck_str = card.rjust(3) + ' '

            # If we have the last card, we don't want to print a new line
            elif card_count == len(self.deck):
                deck_str = deck_str + card.rjust(3)
            
            # For every other instance, we add the card to the string along with a space
            else:
                deck_str = deck_str + card.rjust(3) + ' '
            
            card_count += 1

        return deck_str