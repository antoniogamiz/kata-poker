from enum import Enum


class Hand(Enum):
    RoyalFlush = 10
    StraightFlush = 9
    FourOfAKind = 8
    FullHouse = 7
    Flush = 6
    Straight = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

    def __gt__(self, b):
        return self.value > b.value
