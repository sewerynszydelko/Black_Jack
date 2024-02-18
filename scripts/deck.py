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

    def get_card(self):
        return self.cards.pop(random.randint(0, len(self.cards)-1))

    def shuffling_cards(self):
        random.shuffle(self.cards)
