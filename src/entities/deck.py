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
    value: int


@dataclass(frozen=True)
class Deck:
    cards: [Card]


def createPokerDeck():
    suits = range(4)
    cards: [Card] = []
    for suit in suits:
        id = 0
        cards.append(Card(suit, id, 12))
        id += 1
        for number in range(12):
            cards.append(Card(suit, id, number))
            id += 1
    return Deck(cards)
