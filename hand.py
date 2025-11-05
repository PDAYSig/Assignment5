from card import Card
class Hand:
    NUMBER_OF_CARDS = 13

    def __init__(self):
        self.cards = []

    def __str__(self):
        '''Read'em and weep. 
        This function returns a string containing all the cards in the hand'''
        show_hand = ""
        for card in self.cards:
            if card == self.cards[len(self.cards) - 1]:
                show_hand = show_hand + card.__str__()
            else:
                show_hand = show_hand + f"{card.__str__() :>3}" + " "
        
        if self.cards == None:
            show_hand = "Empty"
        return show_hand
    
    def add_card(self, card : Card):
        '''This function adds a Card object to the hand'''
        self.cards.append(card)



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