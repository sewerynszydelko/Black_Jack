""" Game calls file """
from player import Player
from deck import Deck


class Game:

    def __init__(self) -> None:
        self.score_points = 0

    def __str__(self):
        return f"Your score: {self.score_points}"

    def check_who_win(self, player_1, player_2):
        if player_1.player_points >= 21:
            self.score_points += 1
            return print(f"{player_1.name} win")
        elif player_2.player_points >= 21:
            return print(f"{player_2.name} win")

        if player_1.player_points > player_2.player_points:
            self.score_points += 1
            return print(f"{player_1.name} win")
        else:
            return print(f"{player_2.name} win")

    def save_name_score(self, player_name: str) -> str:
        user_input = input("Do you want to save score? Y or N: ")
        if user_input == "Y":
            with open("score.txt", 'a', encoding="utf-8") as file:
                file.write(f"{player_name}: {self.score_points}\n")
        else:
            print("ok not saved")

    def show_players_scores(self):
        with open("score.txt", "r", encoding="utf-8") as file:
            scors = file.read()
        print(scors)

    def play(self):
        deck = Deck()
        deck.create_deck()
        player = Player(input("Hi give me your name for this game: "))
        crupier = Player("Crupier")
        game_condituion = True

        print("If you want exit any time type exit")
        while game_condituion:

            if len(deck.cards) < 5:
                print("\nGame end not enought cards for you to play")
                print(self)
                self.save_name_score()
                break

            player.pick_card(deck)
            crupier.pick_card(deck)

            player.pick_card(deck)
            crupier.pick_card(deck)

            print("Now you have:")
            print(player)
            print(
                "If you want pick another card type 'yes'\nor no to see who win or exit to exit\n")
            user_input = input()

            if user_input == "exit":
                break

            if user_input == "yes":
                player.pick_card(deck)
                crupier.pick_card(deck)

                player.count_point()
                crupier.count_point()

                self.check_who_win(player, crupier)
                print(self)
            else:
                player.count_point()
                crupier.count_point()

                self.check_who_win(player, crupier)
                print(self)
                input("Pres any key to contiue")


if __name__ == "__main__":
    game = Game()
    game.play()
