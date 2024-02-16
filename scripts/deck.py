""" Deck Class file """
from scripts.card import Card
import random

class Deck:

    def __init__(self):
        self.cards = []

    def create_deck(self):
        for s in Card.symbols:
            for v in Card.values:
                self.cards.append(Card(s,v))
