from dataclasses import dataclass
from enum import Enum


class Pip(Enum):
    ACE = 14
    TWO = 2
    THIR = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    J = 11
    Q = 12
    K = 13


class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


@dataclass(frozen=True)
class Card:
    suit: Suit
    pip: Pip


@dataclass
class Deck:
    cards: [Card]


def create_poker_deck():
    cards: [Card] = []
    for suit in list(CardSuit):
        print(suit)
        for number in list(CardNumber):
            cards.append(Card(suit, number))
    return Deck(cards)
