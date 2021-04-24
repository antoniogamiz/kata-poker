import unittest

from use_cases.hand_comparator import HandComparator
from tests.utils.hand_factory import HandFactory


class TestHandComparatorUseCase(unittest.TestCase):
    hand_factory = HandFactory()

    def test_royal_flush_vs_straight_flush(self):
        royal_flush = self.hand_factory.create_royal_flush()
        straight_flush = self.hand_factory.create_straight_flush()
        winnerIndex = HandComparator.compare([royal_flush, straight_flush])
        self.assertEqual(winnerIndex, 0)

    def test_straight_flush_vs_four_of_a_kind(self):
        straight_flush = self.hand_factory.create_straight_flush()
        four_of_a_kind = self.hand_factory.create_four_of_a_kind()
        winnerIndex = HandComparator.compare([straight_flush, four_of_a_kind])
        self.assertEqual(winnerIndex, 0)

    def test_four_of_a_kind_vs_full_house(self):
        four_of_a_kind = self.hand_factory.create_four_of_a_kind()
        full_house = self.hand_factory.create_full_house()
        winnerIndex = HandComparator.compare([four_of_a_kind, full_house])
        self.assertEqual(winnerIndex, 0)

    def test_full_house_vs_flush(self):
        full_house = self.hand_factory.create_full_house()
        flush = self.hand_factory.create_flush()
        winnerIndex = HandComparator.compare([full_house, flush])
        self.assertEqual(winnerIndex, 0)

    def test_flush_vs_straight(self):
        flush = self.hand_factory.create_flush()
        straight = self.hand_factory.create_straight()
        winnerIndex = HandComparator.compare([flush, straight])
        self.assertEqual(winnerIndex, 0)

    def test_straight_vs_three_of_a_kind(self):
        straight = self.hand_factory.create_straight()
        three_of_a_kind = self.hand_factory.create_three_of_a_kind()
        winnerIndex = HandComparator.compare([straight, three_of_a_kind])
        self.assertEqual(winnerIndex, 0)

    def test_three_of_a_kind_vs_two_pair(self):
        three_of_a_kind = self.hand_factory.create_three_of_a_kind()
        two_pair = self.hand_factory.create_two_pair()
        winnerIndex = HandComparator.compare([three_of_a_kind, two_pair])
        self.assertEqual(winnerIndex, 0)

    def test_two_pair_vs_one_pair(self):
        two_pair = self.hand_factory.create_two_pair()
        one_pair = self.hand_factory.create_one_pair()
        winnerIndex = HandComparator.compare([two_pair, one_pair])
        self.assertEqual(winnerIndex, 0)

    def test_one_pair_vs_high_card(self):
        one_pair = self.hand_factory.create_one_pair()
        high_card = self.hand_factory.create_high_card()
        winnerIndex = HandComparator.compare([one_pair, high_card])
        self.assertEqual(winnerIndex, 0)

    def test_royal_flush_vs_straight_flush_vs_high_card(self):
        straight_flush_1 = self.hand_factory.create_lower_straight_flush()
        straight_flush_2 = self.hand_factory.create_straight_flush()
        high_card = self.hand_factory.create_high_card()
        winnerIndex = HandComparator.compare(
            [straight_flush_1, straight_flush_2])
        self.assertEqual(winnerIndex, 1)
