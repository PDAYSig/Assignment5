from typing import Union
class Card:
    def __init__(self, rank : Union[str, int], suit : str):
        # super().__init__()
        self.suit = suit
        '''If we cannot make the rank an integer, it must mean that the card is
            a Jack, Queen, King, or Ace so we must assign them values specially'''
        try:
            self.rank = int(rank)
        except:
            if rank == 'J':
                self.rank = 11
            elif rank == 'Q':
                self.rank = 12
            elif rank == 'K':
                self.rank = 13
            elif rank == 'A':
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