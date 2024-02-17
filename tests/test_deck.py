""" Test Deck class  """
from scripts.deck import Deck

test_deck = Deck()


def test_cards():
    assert test_deck.cards == []


def test_create_deck():
    test_deck.create_deck()

    assert len(test_deck.cards) == 52


def test_pick_card():
    test_deck.pick_card()

    assert len(test_deck.cards) == 51
