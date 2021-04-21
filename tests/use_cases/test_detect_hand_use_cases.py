import unittest

from src.entities.deck import Card
from src.entities.hand import Hand
from src.use_cases.hand_detector import HandDetector
from tests.utils.hand_factory import HandFactory


class TestDetectHandUseCase(unittest.TestCase):
    hand_detector = HandDetector()
    hand_factory = HandFactory()

    def test_royal_flush(self):
        hand = self.hand_factory.create_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.RoyalFlush)

    def test_almost_royal_flush(self):
        hand = self.hand_factory.create_almost_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.HighCard)

    def test_straight_flush(self):
        hand = self.hand_factory.create_straight_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.StraightFlush)

    def test_unordered_royal_flush(self):
        hand = self.hand_factory.create_unordered_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.RoyalFlush)

    def test_four_of_a_kind(self):
        hand = self.hand_factory.create_four_of_a_kind()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.FourOfAKind)

    def test_full_house(self):
        hand = self.hand_factory.create_full_house()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.FullHouse)

    def test_flush(self):
        hand = self.hand_factory.create_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Flush)

    def test_straight(self):
        hand = self.hand_factory.create_straight()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Straight)

    def test_three_of_a_kind(self):
        hand = self.hand_factory.create_three_of_a_kind()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.ThreeOfAKind)

    def test_two_pair(self):
        hand = self.hand_factory.create_two_pair()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.TwoPair)

    def test_one_pair(self):
        hand = self.hand_factory.create_one_pair()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.OnePair)

    def test_high_card(self):
        hand = self.hand_factory.create_high_card()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.HighCard)
