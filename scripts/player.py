""" Player class file """
from deck import Deck
from card import Card


class Player(Deck):

    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.player_points = 0

    def __str__(self):
        return f"Player: {self.name}\nCards: {self.player_cards}"

    def pick_card(self, deck_obj):
        self.player_cards.append(deck_obj.get_card())

    def count_point(self):
        for card in self.player_cards:
            self.player_points += Card.values[card.get_value()]
        self.player_cards.clear()
