from enum import Enum


class CardSuit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

    def __eq__(self, other):
        if isinstance(other, CardSuit):
            return self.value == other.value

    def __gt__(self, other):
        if isinstance(other, CardSuit):
            return self.value > other.value

    def __lt__(self, other):
        if isinstance(other, CardSuit):
            return self.value < other.value

    def __le__(self, other):
        if isinstance(other, CardSuit):
            return not self > other

    def __ge__(self, other):
        if isinstance(other, CardSuit):
            return not self < other

    # I decided not to implement hash here



