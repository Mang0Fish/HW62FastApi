from card_rank import CardRank
from card_suit import CardSuit
from card import Card
from deck_error import DeckCheatingError
import random
from copy import deepcopy
from deck_interface import IDeck
from typing import override


def fair_deck(func):
    """This decorator checks if the shuffling worked as it should"""
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        a = deepcopy(a)
        b = func(*args, **kwargs)
        if a == b:
            raise DeckCheatingError("Cheating detected! Decks not shuffled properly!")
        else:
            return a
    return wrapper


class Deck(IDeck):
    def __init__(self, shuffle=True):
        """The Deck constructor, adds cards and shuffles them if the user wants"""
        self._cards = []
        for h in CardSuit:
            for j in CardRank:
                self._cards.append(Card(h, j))
        if shuffle:
            self.shuffle()
        self._index = 0

    @property
    @override
    def cards(self):
        """Returns the cards"""
        return self._cards

    @fair_deck
    @override
    def shuffle(self):
        """Shuffles the cards"""
        random.shuffle(self._cards)
        return self.cards

    @override
    def draw(self):
        """Draw one card from the decks start"""
        if self.cards:
            return self._cards.pop(0)
        # Returns None anyway

    @override
    def add_card(self, card):
        """Adds a card to the decks end"""
        self._cards.append(card)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        if isinstance(item, int) and -len(self) <= item < len(self):
            return self.cards[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self):
            raise StopIteration
        card = self.cards[self._index]
        self._index += 1
        return card




