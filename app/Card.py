class Card:
    def __init__(self, suit, point):
        self.suit = suit
        self.point = point

    def get_points(self):
        return self.point.value

    def __str__(self):
        return f"{self.suit.value}-{self.point.name}"
