""" Game calls file """
from player import Player
from deck import Deck

class Game:

    def __init__(self) -> None:
        ...

    def check_who_win(self,player_1,player_2):
        if player_1.player_points >= 28:
            return f"{player_1.name} win"
        elif player_2.player_points >= 28:
            return f"{player_2.name} win"

        if player_1.player_points > player_2.player_points:
            return f"{player_1.name} win"
        else:
            return f"{player_2.name} win"

    # TODO - Decide who win
    # TODO - Loop for game
    # TODO - Save name and score
    # TODO - make quit option
    # TODO - Exeption clas for game

t_deck = Deck()
test_player = Player("sew")
player_2 = Player("crupier")

t_deck.create_deck()

test_player.pick_card(t_deck)
test_player.pick_card(t_deck)
test_player.count_point()

player_2.pick_card(t_deck)
player_2.pick_card(t_deck)
player_2.count_point()

new_game = Game()
print(new_game.check_who_win(test_player,player_2))