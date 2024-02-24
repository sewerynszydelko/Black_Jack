""" Game calls file """
from player import Player
from deck import Deck


class Game:
    """Class handle game logic
    """

    def __init__(self) -> None:
        """initalize score_points of player, not crupier
        """
        self.score_points = 0

    def __str__(self) -> str:
        """
        Returns:
            str: Info about score player
        """
        return f"Your score: {self.score_points}"

    def check_who_win(self, player_1: object, player_2: object) -> None:
        """Compare points of player 1 and player 2
        Args:
            player_1 (object): player obj
            player_2 (object): crupier obj
        Returns:
            None,int: Add point to game class and print out info who win
        """
        if player_1.player_points >= 21:
            self.score_points += 1
            return print(f"{player_1.name} win\n")
        elif player_2.player_points >= 21:
            return print(f"{player_2.name} win\n")

        if player_1.player_points > player_2.player_points:
            self.score_points += 1
            return print(f"{player_1.name} win\n")
        else:
            return print(f"{player_2.name} win\n")

    def save_name_score(self, player_name: str) -> str:
        """Save player name with his score in local 'score.txt'
        Args:
            player_name (str): Name of player
        Returns:
            str: save file or print out info
        """
        user_input = input("Do you want to save score? Y or N: ")
        if user_input == "Y" or user_input == "y":
            with open("score.txt", 'a', encoding="utf-8") as file:
                file.write(f"{player_name}: {self.score_points}\n")
        else:
            print("ok not saved\n THANKS FOR PLAYING")

    def show_players_scores(self):
        """Load socre and players from local 'score.txt'
        if not existed will create
        """
        try:
            with open("score.txt", "r", encoding="utf-8") as file:
                scors = file.read()
        except FileNotFoundError:
            print("File not found! , creating file..")
            with open("score.txt", "w", encoding="utf-8") as file:
                file.write("")
            print("file created")

        print(scors)

    def play(self):
        """Main method of game to play game and intilaze all necesery obj
        """
        deck = Deck()
        deck.create_deck()
        player = Player(input("Hi give me your name for this game: "))
        crupier = Player("Crupier")
        game_condituion = True

        print("\nIf you want exit any time type exit")
        while game_condituion:

            if len(deck.cards) < 1:
                print("\nGame end not enought cards for you to play")
                print(self)
                self.save_name_score(player_name=player.name)
                break

            # Piciking Cards 2x times
            player.pick_card(deck)
            crupier.pick_card(deck)

            player.pick_card(deck)
            crupier.pick_card(deck)

            # Print info and get user input
            print("Now you have:")
            print(player)
            print(
                "If you want pick another card type 'yes'\nor no to see who win or exit to exit")
            user_input = input(".. ")

            if user_input == "exit":
                break

            if user_input == "yes":
                player.pick_card(deck)
                crupier.pick_card(deck)

                print(player)

                player.count_point()
                crupier.count_point()

                self.check_who_win(player, crupier)

                # Show points of player and crupier
                player.print_points()
                crupier.print_points()
                print("\n")

                # Clear points of player and crupier
                player.clear_points()
                crupier.clear_points()

                print(self)
            else:
                player.count_point()
                crupier.count_point()

                self.check_who_win(player, crupier)

                player.print_points()
                crupier.print_points()
                print("\n")

                player.clear_points()
                crupier.clear_points()

                print(self)
                input("Pres any key to contiue\n")


if __name__ == "__main__":
    game = Game()
    game.play()
