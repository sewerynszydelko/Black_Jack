""" Deck Class file """
from card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards.clear()
        for s in Card.symbols:
            for v in Card.values:
                self.cards.append(Card(s, v))

    def pick_card(self):
        random.shuffle(self.cards)
        return self.cards.pop(random.randint(0, len(self.cards)))
