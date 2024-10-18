class Move:
    def __init__(self, player, card):
        self.player = player
        self.card = card

    def __str__(self):
        return f"Move: {self.player.__class__.__name__} {self.player} took {self.card} for {self.card.get_points()} points"

