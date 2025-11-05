from typing import Union
class Card:
    ACE_VALUE = 15 # Since the ace has a different value in different games, We make its value a constant for scalability

    FACE_CARDS = {
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : ACE_VALUE
        }
    def __init__(self, rank : Union[str, int], suit : str):
        self.suit = suit
        '''If we cannot make the rank an integer, it must mean that the card is
            a Jack, Queen, King, or Ace so we must assign them values specially'''

        try:
            self.rank = int(rank)
        except ValueError:
            if rank in Card.FACE_CARDS:
                self.rank = Card.FACE_CARDS[rank]


    def __str__(self):
        if self.rank >= 11:
            target_rank = self.rank
            for letter_value, numerical_value in Card.FACE_CARDS.items():
                if numerical_value == target_rank:
                    print_rank = letter_value
        else:
            print_rank = self.rank

        str_return = f'{print_rank}{self.suit}'
        return str_return.rjust(3)


