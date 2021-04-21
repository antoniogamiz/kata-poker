import unittest

from src.entities.deck import Card
from src.entities.hand import Hand
from src.use_cases.hand_detector import HandDetector


class TestDetectHandUseCase(unittest.TestCase):
    hand_detector = HandDetector()

    def test_royal_flush(self):
        hand = self._create_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.RoyalFlush)

    def test_straight_flush(self):
        hand = self._create_straight_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.StraightFlush)

    def test_unordered_royal_flush(self):
        hand = self._create_unordered_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.RoyalFlush)

    def test_poker(self):
        hand = self._create_poker()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.FourOfAKind)

    def test_empty_hand(self):
        hand = self._create_empty_hand()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Empty)

    def _create_royal_flush(self):
        return [Card(1, i, 0) for i in range(5)]

    def _create_straight_flush(self):
        hand = [Card(1, i+9, 0) for i in range(4)]
        hand.append(Card(1, 0, 0))
        return hand

    def _create_unordered_royal_flush(self):
        return [Card(1, 5, 0), Card(1, 4, 0), Card(1, 2, 0), Card(1, 3, 0), Card(1, 1, 0)]

    def _create_empty_hand(self):
        return [Card(1, 7, 0), Card(2, 4, 0), Card(3, 2, 0), Card(3, 3, 0), Card(0, 1, 0)]

    def _create_poker(self):
        hand = [Card(i, 1, 0) for i in range(4)]
        hand.append(Card(1, 0, 0))
        return hand
