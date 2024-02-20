""" Game calls file """
from player import Player
from deck import Deck


class Game:

    def __init__(self) -> None:
        self.score_points = 0

    def check_who_win(self, player_1, player_2):
        if player_1.player_points >= 28:
            self.score_points += 1
            return f"{player_1.name} win"
        elif player_2.player_points >= 28:
            return f"{player_2.name} win"

        if player_1.player_points > player_2.player_points:
            self.score_points += 1
            return f"{player_1.name} win"
        else:
            return f"{player_2.name} win"

    # TODO - Loop for game
        # TODO - make quit option
        
    def save_name_score(self, player_name: str) -> str:
        with open("score.txt", 'a', encoding="utf-8") as file:
            file.write(f"{player_name}: {self.score_points}\n")

    def show_players_scores(self):
        with open("score.txt","r",encoding="utf-8") as file:
            scors =file.read()
        print(scors)

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
print(new_game.check_who_win(test_player, player_2))

new_game.save_name_score(test_player.name)
new_game.show_players_scores()