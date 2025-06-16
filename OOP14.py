from abc import ABC, abstractmethod
from typing import override


class ISpaceship(ABC):

    @abstractmethod
    def get_attack(self):
        pass

    @abstractmethod
    def get_defence(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_details(self):
        pass


class Spaceship(ISpaceship):
    @override
    def get_defence(self):
        return 0

    @override
    def get_attack(self):
        return 0

    @override
    def get_weight(self):
        return 0

    @override
    def get_details(self):
        return "Spaceship"

    def __str__(self):
        return f"{self.get_details()}: Attack: {self.get_attack()}, Defence: {self.get_defence()}, Weight: {self.get_weight()}, "

# return f"Spaceship: Attack:{self.attack}, Defence:{self.defence}, Total Weight:{self.defence} "


class SpaceshipDecorator(ISpaceship, ABC):

    def __init__(self, spaceship):
        self.spaceship = spaceship

    @abstractmethod
    def get_attack(self):
        pass

    @abstractmethod
    def get_defence(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

    def __str__(self):
        return f"Spaceship, Equipment: {self.get_details()}, Attack: {self.get_attack()}, Defence: {self.get_defence()}, Weight: {self.get_weight()}"


class ShieldDecorator(SpaceshipDecorator):

    def get_defence(self):
        return self.spaceship.get_defence() + 10

    def get_weight(self):
        return self.spaceship.get_weight() + 20

    def get_attack(self):
        return self.spaceship.get_attack() + 0

    def get_details(self):
        return f"{self.spaceship.get_details()} Standard Shield"


class WeaponDecorator(SpaceshipDecorator):

    def get_defence(self):
        return self.spaceship.get_defence() + 0

    def get_weight(self):
        return self.spaceship.get_weight() + 15

    def get_attack(self):
        return self.spaceship.get_attack() + 15

    def get_details(self):
        return f"{self.spaceship.get_details()} Laser Gun"


bs = Spaceship()
print(bs)
ws = WeaponDecorator(bs)
ss = ShieldDecorator(ws)
print(ws, ss)



















