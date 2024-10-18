from app.Deck import Deck
from app.Dealer import Dealer
from app.BlackJackPlayer import BlackjackPlayer
from app.Move import Move
from app.Point import Point

class BlackjackGame:
    def __init__(self, player_name):
        self.deck = Deck()
        self.dealer = Dealer("Steve")
        self.player = BlackjackPlayer(player_name)
        self.moves = []
        self.hidden_dealer_card = None

    def play(self):
        self.hidden_dealer_card = self.deck.remove_one_card()

        # Deal initial cards
        self.give_new_card(self.dealer)
        self.give_new_card(self.player)

        # Player's turn
        while self.player.can_play() and self.player.want_to_play() and not self.game_ended():
            self.give_new_card(self.player)

        # Dealer's turn
        if not self.game_ended():
            self.give_card(self.dealer, self.hidden_dealer_card)
            while self.dealer.can_play() and not self.game_ended():
                self.give_new_card(self.dealer)

        self.show_game_winner()

    def give_new_card(self, player):
        self.give_card(player, self.deck.remove_one_card())

    def give_card(self, player, card):
        move = Move(player, card)
        self.moves.append(move)
        player.add_card(card)
        print(f"{move} ({player.get_total_points()})")

    def game_ended(self):
        if self.player.get_total_points() >= 21 or self.dealer.get_total_points() >= 21:
            return True
        return False

    def show_game_winner(self):
        player_points = self.player.get_total_points()
        dealer_points = self.dealer.get_total_points()

        if player_points > 21:
            print(f"{self.player} has lost... {player_points} > 21")
        elif dealer_points > 21:
            print(f"{self.dealer} has lost... {dealer_points} > 21")
        elif player_points > dealer_points:
            print(f"{self.player} wins with {player_points} points!")
        else:
            print(f"{self.dealer} wins with {dealer_points} points!")


if __name__ == "__main__":
    game = BlackjackGame("Samuel")
    game.play()
