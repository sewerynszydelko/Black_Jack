
class Card:
    symbols = ["♥️", "♠", "♣️", "♦️"]
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
              "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 10}

    def __init__(self) -> None:
        self._symbols = self.symbols
        self._values = self.values

    def __repr__(self):
        return f"{self._symbols} -> {self._values}"
