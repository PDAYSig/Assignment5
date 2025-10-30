import random

class Deck():
    def __init__(self):
        self.__card_count = 52
        self.__cards = [
                        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', 
                        '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', 
                        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', 
                        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'
                        ]

    def shuffle(self):
        random.shuffle(self.__cards)

    def deal(self):
        self.__card_count -= 1
        return self.__cards.pop()

    def __str__(self):
        deck_str = ""
        card_count = 0
        for card in self.__cards:
            if card_count % 13 == 0:
                deck_str = deck_str + f"\n{card}"
            else:
                deck_str = deck_str + f" {card}"
            card_count += 1

        return deck_str
    

