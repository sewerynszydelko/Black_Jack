""" Card file class """


class Card:
    symbols = ["♥️", "♠", "♣️", "♦️"]
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 10}

    def __init__(self, symbol: str, values: dict) -> None:
        """Initalize card
        Args:
            symbol (list[str]): symbol of card
            values (dict): might be dict , list or int values of cards
        """
        self._symbol = symbol
        self._value = values

    def __repr__(self):
        return f"{self._symbol} - {self._value}"
