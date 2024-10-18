from app.Player import Player

class BlackjackPlayer(Player):
    def want_to_play(self):
        return self.get_total_points() < 17