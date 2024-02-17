""" Player class file """
from card import Card

class Player(Card):

    def __init__(self,name):
        self.name = name
        self.player_cards = []
        self.player_points = 0
