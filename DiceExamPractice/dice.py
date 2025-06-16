import random
from enum import Enum


class DiceType(Enum):
    """This class is an Enum class that represents multiple dice types
    Each value holds the number of sides a die has,"""

    D4 = 4
    D6 = 6
    D8 = 8
    D12 = 12
    D20 = 20

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def seed(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            random.seed(num)
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Dice:
    def __init__(self, diceType: DiceType):
        self._type = diceType
        self._value = random.randint(1, self._type.value)

    @property
    def type(self):
        return self._type.name

    @property
    def value(self):
        return self._value

    @seed(13)
    def roll(self):
        self._value = random.randint(1, self._type.value)
        return self.value

    def __eq__(self, other):
        if isinstance(other, Dice):
            return self.value == other.value
        else:
            raise TypeError("You need to compare dices")

    def __lt__(self, other):
        if isinstance(other, Dice):
            return self.value < other.value
        else:
            raise TypeError("You need to compare dices")

    def __gt__(self, other):
        if isinstance(other, Dice):
            return self.value > other.value
        else:
            raise TypeError("You need to compare dices")

    def __hash__(self):
        return hash(self.value)

    def __getitem__(self, item):
        l: list[int] = []
        for i in range(item):
            l.append(self.roll())
        return l


if __name__ == "__main__":
    d6_first = Dice(DiceType.D6)
    d6_second = Dice(DiceType.D6)
    print(f"First D6 value: {d6_first.value}")
    print(f"Second D6 value: {d6_second.value}")
    print(f"First D6 rolled again: {d6_first.roll()}")
    if d6_first > d6_second:
        print(f"First D6 shows a higher number ({d6_first.value}) than Second D6 ({d6_second.value})")
    else:
        print(
            f"Second D6 shows a higher number ({d6_second.value}) than or equal to First D6 ({d6_first.value})")
    d20 = Dice(DiceType.D20)
    print(f"Rolling D20 five times: {d20[5]}")







