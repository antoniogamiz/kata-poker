import unittest
from src.entities.deck import Card
from src.entities.hand import Hand
from src.use_cases.hand_detector import HandDetector


class TestDetectHandUseCase(unittest.TestCase):

    def test_royal_flush(self):
        hand_detector = HandDetector()
        hand = self._create_royal_flush()
        self.assertEqual(hand_detector.detect_hand(hand), Hand.RoyalFlush)

    def test_best_royal_flush(self):
        hand_detector = HandDetector()
        hand = self._create_best_royal_flush()
        self.assertEqual(hand_detector.detect_hand(hand), Hand.RoyalFlush)

    def test_unordered_royal_flush(self):
        hand_detector = HandDetector()
        hand = self._create_unordered_royal_flush()
        self.assertEqual(hand_detector.detect_hand(hand), Hand.RoyalFlush)

    def test_empty_hand(self):
        hand_detector = HandDetector()
        hand = self._create_empty_hand()
        self.assertEqual(hand_detector.detect_hand(hand), Hand.Empty)

    def _create_royal_flush(self):
        return [Card(1, i, 0) for i in range(5)]

    def _create_best_royal_flush(self):
        hand = [Card(1, i+9, 0) for i in range(4)]
        hand.append(Card(1, 0, 0))
        return hand

    def _create_unordered_royal_flush(self):
        return [Card(1, 5, 0), Card(1, 4, 0), Card(1, 2, 0), Card(1, 3, 0), Card(1, 1, 0)]

    def _create_empty_hand(self):
        return [Card(1, 7, 0), Card(2, 4, 0), Card(3, 2, 0), Card(3, 3, 0), Card(0, 1, 0)]
