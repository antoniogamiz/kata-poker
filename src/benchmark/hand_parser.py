import random

from entities.deck import Card, Pip, Suit
from use_cases.hand_parser import HandParser


def generate_card():
    suit = random.choice(list(Suit))
    pip = random.choice(list(Pip))
    return Card(suit, pip)


def generate_hand():
    return [generate_card() for i in range(5)]
