from enum import Enum
from entities import Card


class Hand(Enum):
    RoyalFlash = 1
    StraightFlush = 2
    FourOfAKind = 3
    FullHouse = 4
    Flush = 5
    Straight = 6
    ThreeOfAKind = 7
    TwoPair = 8
    OnePair = 9
    HighCard = 10
