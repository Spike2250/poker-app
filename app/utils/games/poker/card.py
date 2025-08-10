from enum import Enum

from pydantic import BaseModel


class Suit(str, Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"


rank_order = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13,
    'A': 14
}


class Rank(str, Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "T"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    @property
    def strength(self) -> int:
        return rank_order[self.value]

    def __lt__(self, other):
        return self.strength < other.strength


class Card(BaseModel):
    suit: Suit
    rank: Rank

    @property
    def symbol(self) -> str:
        """Представление в виде символа (например, A♠)"""
        return f"{self.rank.value}{self.suit.value}"

    def __str__(self):
        return self.symbol

    @property
    def strength(self) -> int:
        return self.rank.strength

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.strength < other.strength
