from scripts.game import Game
from scripts.player import Player

test_game = Game()

def test_check_who_win():
    test_player = Player("test_1")
    test_crupier = Player("test_2")

    test_player.player_points = 2
    test_crupier.player_points = 4

    test_game.check_who_win(test_player,test_crupier)

    assert test_game.score_points == 1