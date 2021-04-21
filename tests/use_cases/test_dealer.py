import unittest

from src.use_cases.dealer import Dealer
from src.entities.deck import Card


class TestDealer(unittest.TestCase):

    DECK_CARD_NUMBER = 13 * 4

    def test_when_next_card_is_requested_then_a_card_is_returned(self):
        dealer = Dealer()
        card = dealer.next_card()

        self.assertIs(type(card), Card)
        self.assertEqual(len(dealer.deck.cards), self.DECK_CARD_NUMBER - 1)

    def test_when_next_cards_are_requested_then_cards_are_returned(self):
        dealer = Dealer()
        number_of_cards_requested = 5
        cards = dealer.next_cards(number_of_cards_requested)

        [self.assertIs(type(card), Card) for card in cards]
        self.assertEqual(len(dealer.deck.cards),
                         self.DECK_CARD_NUMBER - number_of_cards_requested)
