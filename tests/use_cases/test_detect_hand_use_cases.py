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

    def test_almost_royal_flush(self):
        hand = self._create_almost_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Straight)

    def test_straight_flush(self):
        hand = self._create_straight_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.StraightFlush)

    def test_unordered_royal_flush(self):
        hand = self._create_unordered_royal_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.RoyalFlush)

    def test_four_of_a_kind(self):
        hand = self._create_four_of_a_kind()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.FourOfAKind)

    def test_full_house(self):
        hand = self._create_full_house()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.FullHouse)

    def test_flush(self):
        hand = self._create_flush()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Flush)

    def test_straight(self):
        hand = self._create_straight()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.Straight)

    def test_three_of_a_kind(self):
        hand = self._create_three_of_a_kind()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.ThreeOfAKind)

    def test_two_pair(self):
        hand = self._create_two_pair()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.TwoPair)

    def test_one_pair(self):
        hand = self._create_one_pair()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.OnePair)

    def test_high_card(self):
        hand = self._create_high_card()
        expected_hand = self.hand_detector.detect_hand(hand)
        self.assertEqual(expected_hand, Hand.HighCard)

    def _create_royal_flush(self):
        return [Card(1, i, 0) for i in range(5)]

    def _create_almost_royal_flush(self):
        return [Card(1+i, i, 0) for i in range(5)]

    def _create_straight_flush(self):
        hand = [Card(1, i+8, 0) for i in range(5)]
        return hand

    def _create_unordered_royal_flush(self):
        return [Card(1, 0, 0), Card(1, 4, 0), Card(1, 2, 0), Card(1, 3, 0), Card(1, 1, 0)]

    def _create_four_of_a_kind(self):
        hand = [Card(i, 1, 0) for i in range(4)]
        hand.append(Card(1, 0, 0))
        return hand

    def _create_full_house(self):
        hand = [Card(i, 10, 0) for i in range(3)]
        hand.append(Card(1, 9, 0))
        hand.append(Card(2, 9, 0))
        return hand

    def _create_flush(self):
        return [Card(1, 1, 0), Card(1, 3, 0), Card(
            1, 4, 0), Card(1, 5, 0), Card(1, 6, 0)]

    def _create_straight(self):
        return [Card(1+i, i, 0) for i in range(5)]

    def _create_three_of_a_kind(self):
        return [Card(1, 1, 0), Card(2, 1, 0), Card(
            3, 1, 0), Card(2, 2, 0), Card(1, 3, 0)]

    def _create_two_pair(self):
        return [Card(1, 1, 0), Card(2, 1, 0), Card(
            1, 2, 0), Card(2, 2, 0), Card(1, 3, 0)]

    def _create_one_pair(self):
        return [Card(1, 6, 0), Card(2, 1, 0), Card(
            1, 2, 0), Card(2, 2, 0), Card(1, 3, 0)]

    def _create_high_card(self):
        return [Card(1, 7, 0), Card(2, 4, 0), Card(3, 2, 0), Card(3, 3, 0), Card(0, 1, 0)]
