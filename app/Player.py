from app.Point import Point

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_total_points(self):
        min_total = 0
        max_total = 0
        for card in self.hand:
            points = card.get_points()
            min_total += points
            max_total += 11 if card.point == Point.C_ACE_1 else points
        return max_total if max_total <= 21 else min_total

    def add_card(self, card):
        self.hand.append(card)

    def __str__(self):
        return self.name

    def can_play(self):
        return self.get_total_points() < 21

    def want_to_play(self):
        raise NotImplementedError