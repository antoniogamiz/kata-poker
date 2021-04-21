import unittest

from src.use_cases.hand_comparator import HandComparator
from tests.utils.hand_factory import HandFactory


class TestHandComparatorUseCase(unittest.TestCase):
    hand_factory = HandFactory()

    def test_royal_flush_vs_straight_flush(self):
        royal_blush = self.hand_factory.create_royal_flush()
        straight_flush = self.hand_factory.create_straight_flush()
        winnerIndex = HandComparator.compare([royal_blush, straight_flush])
        self.assertEqual(winnerIndex, 0)
