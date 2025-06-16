class Card:
    def __init__(self, suit, rank, face_up=True):
        """The card constructor, builds the card by suit and rank, and the user can decide whether
        the card is revealed or not, (Revealed in default)"""
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    @property
    def suit(self):
        """Returns the cards suit"""
        return self._suit

    @property
    def rank(self):
        """Returns the cards rank"""
        return self._rank

    @property
    def face_up(self):
        """Returns True if the card is revealed, False if not"""
        return self._face_up

    def flip(self):
        """Flips the cards face, switching the face_up value"""
        self._face_up = not self._face_up
        return self.face_up

    def get_display_name(self):
        """Returns the cards suit and rank in a formated string"""
        return f"{self._rank.name} of {self._suit.name}"

    def __eq__(self, other):
        if isinstance(other, Card):
            return self._suit == other.suit and self._rank == other.rank

    def __lt__(self, other):
        if isinstance(other, Card):
            if self._rank == other.rank:
                return self._suit < other.suit
            else:
                return self._rank < other.rank

    def __gt__(self, other):
        if isinstance(other, Card):
            if self._rank == other.rank:
                return self._suit > other.suit
            else:
                return self._rank > other.rank

    def __le__(self, other):
        if isinstance(other, Card):
            return not self > other

    def __ge__(self, other):
        if isinstance(other, Card):
            return not self < other

    def __hash__(self):
        return hash(self._suit + self._rank)

    def __str__(self):
        if self._face_up:
            return self.get_display_name()
        else:
            return "?"

    def __repr__(self):
        return f"Card({self._suit}, {self._rank}, {self._face_up})"


