""" Player file Class tests """
from scripts.player import Player, Deck
from scripts.card import Card

test_deck = Deck()
test_player = Player("sew")

def test_pick_card():
    test_deck.create_deck()

    test_player.pick_card(test_deck)
    test_player.pick_card(test_deck)

    assert len(test_player.player_cards) == 2


def test_player_name():
    assert test_player.name == "sew"

def test_counting_points():
    test_player.count_point()

    assert test_player.player_points == int(Card.values[test_player.player_cards[0].get_value()]) + int(Card.values[test_player.player_cards[1].get_value()])