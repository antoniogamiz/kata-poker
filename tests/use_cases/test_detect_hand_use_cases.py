import unittest
from src.entities.hand import Hand
from src.use_cases.hand_detector import detect_royal_flush


class TestDetectHandUseCase(unittest.TestCase):

    def test_royal_flush(self):
        hand = []
        self.assertEqual(detect_royal_flush(hand), Hand.RoyalFlush)

    def _create_royal_flush():
        return [Card(2, 1), Card(3, 1), Card(4, 1), Card(5, 1), Card(6, 1)]
