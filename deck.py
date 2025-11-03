import random
'''
This file contains the Deck class. It is used to keep track of which cards are in the deck
as well as shuffling and dealing the cards.
'''


class Deck:
    def __init__(self):
        self.__card_count = 52
        self.__cards = [
                        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', 
                        '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', 
                        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', 
                        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'
                        ]

    def shuffle(self):
        '''This function is used to shuffle the cards'''
        random.shuffle(self.__cards)

    def deal(self):
        '''This function deals a single card from the deck'''
        self.__card_count -= 1
        return self.__cards.pop()

    def __str__(self):
        deck_str = ""
        card_count = 0
        for card in self.__cards:
            #we check if the card count is a multiple of 13
            if card_count % 13 == 0:
                deck_str = deck_str + f"\n{card :>3}"
            else:
                deck_str = deck_str + f" {card :>3}"
            card_count += 1

        return deck_str
    

