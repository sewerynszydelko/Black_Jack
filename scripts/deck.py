""" Deck Class file """
from card import Card
import random


class Deck:
    """Deck of cards for Black Jack
    """

    def __init__(self):
        self.cards = []

    def create_deck(self):
        """create deck of cards
        """
        self.cards.clear()
        for s in Card.symbols:
            for v in Card.values:
                self.cards.append(Card(s, v))

    def get_card(self):
        """ Get card to varible
        Returns:
            card(str) : pop it card from deck 
        """
        return self.cards.pop(random.randint(0, len(self.cards)-1))

    def shuffling_cards(self):
        """suffle cards in deck
        """
        random.shuffle(self.cards)
