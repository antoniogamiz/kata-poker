from dataclasses import dataclass


@dataclass(frozen=True)
class CardNumber:
    id: int


@dataclass(frozen=True)
class CardSuit:
    id: int


@dataclass(frozen=True)
class Card:
    suit: CardSuit
    number: CardNumber


@dataclass(frozen=True)
class Deck:
    cards: [Card]


def createPokerDeck():
    suits = range(4)
    numbers = range(13)
    cards: [Card] = []
    for suit in suits:
        for number in numbers:
            cards.append(Card(suit, number))
    return Deck(cards)
