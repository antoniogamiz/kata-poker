from src.entities.deck import Deck, create_poker_deck
import random


class Dealer:
    deck: Deck

    def __init__(self):
        self.deck = create_poker_deck()
        random.shuffle(self.deck.cards)

    def next_card(self):
        return self.deck.cards.pop()

    def next_cards(self, n):
        return [self.deck.cards.pop() for i in range(n)]
