from Deck import Deck
class Card(Deck):
    def __init__(self, card : str):
        # super().__init__()
        self.suit = card[len(card) - 1]
        try:
            self.rank = int(card[:len(card) - 1])
        except ValueError:
            '''If we cannot make the rank an integer, it must mean that the card is
            a Jack, Queen, King, or Ace so we must assign them values specially'''
            if card[:len(card) - 1] == 'J':
                self.rank = 11
            elif card[:len(card) - 1] == 'Q':
                self.rank = 12
            elif card[:len(card) - 1] == 'K':
                self.rank = 13
            elif card[:len(card) - 1] == 'A':
                self.rank = 14
    
    def __str__(self):
        if self.rank == 11:
            print_rank = 'J'
        elif self.rank == 12:
            print_rank = 'Q'
        elif self.rank == 13:
            print_rank = 'K'
        elif self.rank == 14:
            print_rank = 'A'
        else:
            print_rank = self.rank

        return f'{print_rank}{self.suit}'