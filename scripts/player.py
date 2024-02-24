""" Player class file """
from deck import Deck
from card import Card


class Player(Deck):
    """Player class
    Args:
        Deck (object): Takes Deck as parent
    """

    def __init__(self, name: str):
        """Initalize player
        Args:
            name (str): name/ str
        """
        self.name = name
        self.player_cards = []
        self.player_points = 0

    def __str__(self):
        return f"Player: {self.name}\nCards: {self.player_cards}"

    def pick_card(self, deck_obj: object):
        """Get card for player
        Args:
            deck_obj (object): dec as obj
        """
        self.player_cards.append(deck_obj.get_card())

    def count_point(self):
        """Count points of cards player and clear that cards
        """
        if "A" in self.player_cards[0]._value or "A" in self.player_cards[1]._value:
            self.player_points -= 9

        for card in self.player_cards:
            self.player_points += Card.values[card.get_value()]
        self.player_cards.clear()

    def clear_points(self):
        self.player_points = 0

    def print_points(self):
        return print(f"{self.name} have:{self.player_points} points")
