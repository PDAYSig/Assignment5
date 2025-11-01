# (6 points) __init__(): An initializer without any parameters.

# (8 points) The Hand class has one public instance variable, cards, 
# for storing a list of up to 13 cards. Additionally, you must have the required constants,
#  as can be seen from the attached programs.

# (8 points) __str__(): 
# The string representation for an instance of a Hand consists of single line containing
#  the strings representation of each card (with a single space after each card). 
# If the hand is empty, the string “Empty” is returned.

# (8 points) add_card(card): Adds the given card to the hand. If the hand is full, then nothing happens.
from card import Card
class Hand:
    def __init__(self):
        NUMBER_OF_CARDS = 13
        self.hand = []

    def __str__(self):
        
        show_cards = ""
        for card in self.hand:
            show_cards = show_cards + card.__str__()
        if self.hand == None:
            show_cards = "Empty"
        return show_cards
    
    def add_card(self, card : Card):
        self.hand.append(card)



def main():
    hand = Hand()
    print(hand)

    ace_of_spades = Card('A', 'S')
    hand.add_card(ace_of_spades)
    print(hand)

main()