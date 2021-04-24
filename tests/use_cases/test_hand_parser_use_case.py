import unittest

from src.entities.deck import Suit, Pip, Card
from src.entities.hand import Hand
from src.use_cases.hand_parser import HandParser
from tests.utils.hand_factory import HandFactory


class TestHandParserUseCase(unittest.TestCase):

    def test_when_the_hand_is_a_royal_flush(self):
        hand = [Card(Suit.SPADES, Pip.ACE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.SPADES, Pip.J),
                Card(Suit.SPADES, Pip.K),
                Card(Suit.SPADES, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.RoyalFlush)

    def test_when_the_hand_is_a_straight_flush(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.SPADES, Pip.J),
                Card(Suit.SPADES, Pip.K),
                Card(Suit.SPADES, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.StraightFlush)

    def test_when_the_hand_is_a_four_of_a_kind(self):
        hand = [Card(Suit.DIAMONDS, Pip.ACE),
                Card(Suit.CLUBS, Pip.ACE),
                Card(Suit.HEARTS, Pip.ACE),
                Card(Suit.SPADES, Pip.ACE),
                Card(Suit.SPADES, Pip.EIGHT)]
        self._assert_hand_is_correctly_parsed(hand, Hand.FourOfAKind)

    def test_when_the_hand_is_a_full_house(self):
        hand = [Card(Suit.DIAMONDS, Pip.ACE),
                Card(Suit.CLUBS, Pip.ACE),
                Card(Suit.HEARTS, Pip.ACE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.CLUBS, Pip.TEN)]
        self._assert_hand_is_correctly_parsed(hand, Hand.FullHouse)

    def test_when_the_hand_is_a_flush(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.SPADES, Pip.TWO),
                Card(Suit.SPADES, Pip.SIX),
                Card(Suit.SPADES, Pip.FOUR),
                Card(Suit.SPADES, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.Flush)

    def test_when_the_hand_is_a_straight(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.CLUBS, Pip.J),
                Card(Suit.SPADES, Pip.K),
                Card(Suit.DIAMONDS, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.Straight)

    def test_when_the_hand_is_a_three_of_a_kind(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.CLUBS, Pip.NINE),
                Card(Suit.SPADES, Pip.K),
                Card(Suit.DIAMONDS, Pip.NINE)]
        self._assert_hand_is_correctly_parsed(hand, Hand.ThreeOfAKind)

    def test_when_the_hand_is_a_two_pair(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.CLUBS, Pip.TEN),
                Card(Suit.CLUBS, Pip.NINE),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.DIAMONDS, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.TwoPair)

    def test_when_the_hand_is_a_one_pair(self):
        hand = [Card(Suit.SPADES, Pip.NINE),
                Card(Suit.CLUBS, Pip.TEN),
                Card(Suit.CLUBS, Pip.EIGHT),
                Card(Suit.SPADES, Pip.TEN),
                Card(Suit.DIAMONDS, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.OnePair)

    def test_when_the_hand_is_a_high_card(self):
        hand = [Card(Suit.SPADES, Pip.FIVE),
                Card(Suit.CLUBS, Pip.TEN),
                Card(Suit.CLUBS, Pip.EIGHT),
                Card(Suit.SPADES, Pip.SEVEN),
                Card(Suit.DIAMONDS, Pip.Q)]
        self._assert_hand_is_correctly_parsed(hand, Hand.HighCard)

    def _assert_hand_is_correctly_parsed(self, hand, expected_hand):
        hand_parser = HandParser()
        parsed_hand = hand_parser.parse(hand)
        self.assertEqual(parsed_hand, expected_hand)
