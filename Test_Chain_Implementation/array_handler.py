from abc import ABC, abstractmethod


class ArrayHandler(ABC):

    def __init__(self):
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @abstractmethod
    def handle(self, array):
        pass
