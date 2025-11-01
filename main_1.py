from Deck import Deck
from Card import Card

def main():
    deck = Deck()
    deck.shuffle()
    print(deck)

    card_1 = Card(deck.deal())
    print(card_1)
    print(deck)
    

if __name__ == "__main__":
    main()