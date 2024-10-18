import random

from app.Suit import Suit
from app.Point import Point
from app.Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for suit in Suit:
            for point in Point:
                self.cards.append(Card(suit, point))

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_one_card(self):
        if len(self.cards) == 0:
            raise RuntimeError("No more cards")
        return self.cards.pop()
