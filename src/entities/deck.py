from dataclasses import dataclass
from enum import Enum


class Pip(Enum):
    ACE = 2
    TWO = 3
    THREE = 5
    FOUR = 7
    FIVE = 11
    SIX = 13
    SEVEN = 17
    EIGHT = 19
    NINE = 23
    TEN = 29
    J = 31
    Q = 37
    K = 41


class Suit(Enum):
    DIAMONDS = 0x0001
    CLUBS = 0x0010
    HEARTS = 0x0100
    SPADES = 0x1000


@dataclass(frozen=True)
class Card:
    suit: Suit
    pip: Pip


@dataclass
class Deck:
    cards: [Card]
