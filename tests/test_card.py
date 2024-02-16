""" Card class test """
from scripts.card import Card


def test_symbols_values():
    test_card = Card(["♥️", "♠", "♣️", "♦️"], {
                     "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, })

    assert test_card._symbol == ["♥️", "♠", "♣️", "♦️"]
    assert test_card._value == {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, }

def test_representation():
    test_card = Card("♥️","2")

    assert test_card 