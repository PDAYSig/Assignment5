from card import Card
from typing import Union
class Hand:
    NUMBER_OF_CARDS = 13

    def __init__(self):
        self.cards = []

    def __str__(self):
        '''Read'em and weep. 
        This function returns a string containing all the cards in the hand'''
        show_hand = ""
        for card in self.cards:
            show_hand = show_hand + f"{card.__str__() :>3}" + " "

        if self.cards == None:
            show_hand = "Empty"
        return show_hand
    
    def add_card(self, card_or_rank, suit= None) -> None:
        '''This function adds a Card object to the hand'''
        if suit == None and type(card_or_rank) == tuple:
            rank, suit = card_or_rank
        else:
            rank = card_or_rank
        self.cards.append(Card(rank, suit))



# def main():
#     cards = Hand()
#     print(cards)

#     ace_of_spades = Card('A', 'S')
#     cards.add_card(ace_of_spades)
#     print(cards)
#     print(ace_of_spades.__str__())
#     ace_of_hearts = Card('A', 'H')
#     cards.add_card(ace_of_hearts)
#     print(cards)


# main()