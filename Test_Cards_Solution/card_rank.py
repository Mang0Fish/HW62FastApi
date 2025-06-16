from enum import Enum


class CardRank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __eq__(self, other):
        if isinstance(other, CardRank):
            return self.value == other.value

    def __gt__(self, other):
        if isinstance(other, CardRank):
            return self.value > other.value

    def __lt__(self, other):
        if isinstance(other, CardRank):
            return self.value < other.value

    def __le__(self, other):
        if isinstance(other, CardRank):
            return not self > other

    def __ge__(self, other):
        if isinstance(other, CardRank):
            return not self < other

    # I decided not to implement hash here

