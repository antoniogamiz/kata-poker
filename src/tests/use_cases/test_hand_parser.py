import unittest

from entities.deck import Suit, Pip, Card
from entities.hand import Hand
from use_cases.hand_parser import HandParser
from tests.utils.string_to_card_mapper import hand_string_to_hand_mapper


class TestHandParserUseCase(unittest.TestCase):

    def test_when_the_hand_is_a_royal_flush(self):
        hand_string = '10♠ J♠ Q♠ K♠ A♠'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.RoyalFlush)

    def test_when_the_hand_is_a_straight_flush(self):
        hand_string = '9♠ 10♠ Q♠ J♠ K♠'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.StraightFlush)

    def test_when_the_hand_is_a_four_of_a_kind(self):
        hand_string = 'A♦ A♣ A♥ A♠ 8♠'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.FourOfAKind)

    def test_when_the_hand_is_a_full_house(self):
        hand_string = 'A♦ A♣ A♥ 10♠ 10♣'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.FullHouse)

    def test_when_the_hand_is_a_flush(self):
        hand_string = '9♠ 2♠ 6♠ 4♠ Q♠'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.Flush)

    def test_when_the_hand_is_a_straight(self):
        hand_string = '9♠ 10♠ J♣ K♠ Q♦'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.Straight)

    def test_when_the_hand_is_a_three_of_a_kind(self):
        hand_string = '9♠ 10♠ 9♣ K♠ 9♦'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.ThreeOfAKind)

    def test_when_the_hand_is_a_two_pair(self):
        hand_string = '9♠ 10♣ 9♣ 10♠ Q♦'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.TwoPair)

    def test_when_the_hand_is_a_one_pair(self):
        hand_string = '9♠ 10♣ 8♣ 10♠ Q♦'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.OnePair)

    def test_when_the_hand_is_a_high_hand(self):
        hand_string = '5♠ 10♣ 8♣ 7♠ Q♦'
        self._assert_hand_is_correctly_parsed(hand_string, Hand.HighCard)

    def _assert_hand_is_correctly_parsed(self, hand_string, expected_hand):
        hand_parser = HandParser()
        parsed_hand = hand_parser.parse(
            hand_string_to_hand_mapper(hand_string))
        self.assertEqual(parsed_hand, expected_hand)
