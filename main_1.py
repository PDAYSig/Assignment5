import random
from card import Card
from deck import Deck
from hand import Hand

def main():
    """The main program for testing the classes Card, Deck and Hand."""

    c1 = Card(10, 'S')
    c2 = Card('J', 'H')
    c3 = Card('10', 'D')

    print(c1, c2, c3)



if __name__ == "__main__":
    main()