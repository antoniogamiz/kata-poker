import unittest

from use_cases.hand_matcher import HandMatcher
from entities.deck import Suit, Pip, Card
from tests.utils.string_to_card_mapper import hand_string_to_hand_mapper


class TestHandMatcher(unittest.TestCase):

    def test_royal_flush_vs_straight_flush(self):
        royal_flush = '10♠ J♠ Q♠ K♠ A♠'
        straight_flush = '9♠ 10♠ J♠ Q♠ K♠'
        self._assert_winner(0, [royal_flush, straight_flush])

    def test_straight_flush_vs_straight_flush(self):
        higher_straight_flush = '9♠ 10♠ J♠ Q♠ K♠'
        lower_straight_flush = '8♠ 9♠ 10♠ J♠ Q♠'
        self._assert_winner(0, [higher_straight_flush, lower_straight_flush])

    def test_straight_flush_vs_poker(self):
        straight_flush = '9♠ 10♠ J♠ Q♠ K♠'
        poker = 'K♦ K♣ K♥ K♠ 8♠'
        self._assert_winner(0, [straight_flush, poker])

    def test_poker_vs_poker(self):
        high_poker = 'A♦ A♣ A♥ A♠ 8♠'
        lower_poker = 'K♦ K♣ K♥ K♠ 8♠'
        self._assert_winner(0, [high_poker, lower_poker])

    def test_poker_vs_poker_with_different_fifth_card(self):
        high_poker = 'A♦ A♣ A♥ A♠ 10♠'
        lower_poker = 'A♦ A♣ A♥ A♠ 8♠'
        self._assert_winner(0, [high_poker, lower_poker])

    def test_poker_vs_full_house(self):
        poker = 'A♦ A♣ A♥ A♠ 10♠'
        full_house = 'A♦ A♣ A♥ 8♠ 8♠'
        self._assert_winner(0, [poker, full_house])

    def test_full_house_vs_full_house_with_different_trio(self):
        high_full_house = 'A♦ A♣ A♥ 8♠ 8♠'
        lower_full_house = 'K♦ K♣ K♥ 8♠ 8♠'
        self._assert_winner(0, [high_full_house, lower_full_house])

    def test_full_house_vs_full_house_with_different_pair(self):
        high_full_house = 'K♦ K♣ K♥ 9♠ 9♠'
        lower_full_house = 'K♦ K♣ K♥ 8♠ 8♠'
        self._assert_winner(0, [high_full_house, lower_full_house])

    def test_full_house_vs_flush(self):
        full_house = 'A♦ A♣ A♥ 8♠ 8♠'
        flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [full_house, flush])

    def test_flush_vs_flush_with_first_higher_card(self):
        high_flush = '2♦ 3♦ 5♦ 7♦ 10♦'
        lower_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [high_flush, lower_flush])

    def test_flush_vs_flush_with_second_higher_card(self):
        high_flush = '2♦ 3♦ 5♦ 8♦ 9♦'
        lower_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [high_flush, lower_flush])

    def test_flush_vs_flush_with_third_higher_card(self):
        high_flush = '2♦ 3♦ 6♦ 7♦ 9♦'
        lower_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [high_flush, lower_flush])

    def test_flush_vs_flush_with_fourth_higher_card(self):
        high_flush = '2♦ 4♦ 5♦ 7♦ 9♦'
        lower_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [high_flush, lower_flush])

    def test_flush_vs_flush_with_fifth_higher_card(self):
        high_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        lower_flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        self._assert_winner(0, [high_flush, lower_flush])

    def test_flush_vs_straight(self):
        flush = '2♦ 3♦ 5♦ 7♦ 9♦'
        straight = '9♠ 10♠ J♣ K♠ Q♦'
        self._assert_winner(0, [flush, straight])

    def test_highest_straight_vs_lowest_straight(self):
        highest_straight = 'A♠ 10♠ J♣ Q♠ K♦'
        lowest_straight = 'A♠ 2♠ 3♣ 4♠ 5♦'
        self._assert_winner(0, [highest_straight, lowest_straight])

    def test_medium_straight_vs_lowest_straight(self):
        medium_straight = '9♠ 10♠ J♣ Q♠ K♦'
        lowest_straight = 'A♠ 2♠ 3♣ 4♠ 5♦'
        self._assert_winner(0, [medium_straight, lowest_straight])

    def test_straight_vs_three_of_a_kind(self):
        straight = 'A♠ 2♠ 3♣ 4♠ 5♦'
        three_of_a_kind = '9♠ 10♠ 9♣ K♠ 9♦'
        self._assert_winner(0, [straight, three_of_a_kind])

    def three_of_a_kind_vs_three_of_a_kind_with_higher_trio(self):
        higher_three_of_a_kind = 'K♠ K♠ 9♣ K♠ 9♦'
        lower_three_of_a_kind = '9♠ 10♠ 9♣ K♠ 9♦'
        self._assert_winner(0, [higher_three_of_a_kind, lower_three_of_a_kind])

    def three_of_a_kind_vs_three_of_a_kind_with_higher_fourth_card(self):
        higher_three_of_a_kind = 'K♠ K♠ 8♣ K♠ 10♦'
        lower_three_of_a_kind = 'K♠ K♠ 9♣ K♠ 9♦'
        self._assert_winner(0, [higher_three_of_a_kind, lower_three_of_a_kind])

    def three_of_a_kind_vs_three_of_a_kind_with_higher_fifth_card(self):
        higher_three_of_a_kind = 'K♠ K♠ 9♣ K♠ 10♦'
        lower_three_of_a_kind = 'K♠ K♠ 9♣ K♠ 9♦'
        self._assert_winner(0, [higher_three_of_a_kind, lower_three_of_a_kind])

    def test_three_of_a_kind_vs_two_pair(self):
        three_of_a_kind = 'K♠ K♠ 9♣ K♠ 9♦'
        two_pair = '9♠ 10♣ 9♣ 10♠ Q♦'
        self._assert_winner(0, [three_of_a_kind, two_pair])

    def test_two_pair_vs_two_pair_when_first_pair_is_higher(self):
        high_two_pair = '8♠ J♣ 8♣ J♠ Q♦'
        low_two_pair = '9♠ 10♣ 9♣ 10♠ Q♦'
        self._assert_winner(0, [high_two_pair, low_two_pair])

    def test_two_pair_vs_two_pair_when_second_pair_is_higher(self):
        high_two_pair = '9♠ 6♣ 9♣ 6♠ Q♦'
        low_two_pair = '9♠ 5♣ 9♣ 5♠ Q♦'
        self._assert_winner(0, [high_two_pair, low_two_pair])

    def test_two_pair_vs_one_pair(self):
        two_pair = '9♠ 10♣ 9♣ 10♠ Q♦'
        one_pair = '9♠ 10♣ 8♣ 10♠ Q♦'
        self._assert_winner(0, [two_pair, one_pair])

    def test_one_pair_vs_one_pair(self):
        higher_one_pair = '9♠ 10♣ 8♣ Q♠ Q♦'
        lower_one_pair = '9♠ 10♣ 8♣ 10♠ Q♦'
        self._assert_winner(0, [higher_one_pair, lower_one_pair])

    def test_one_pair_vs_high_card(self):
        one_pair = '9♠ 10♣ 8♣ 10♠ Q♦'
        high_card = '5♠ 10♣ 8♣ 7♠ Q♦'
        self._assert_winner(0, [one_pair, high_card])

    def test_high_card_vs_high_card(self):
        highest_high_card = '5♠ 9♣ 8♣ 7♠ Q♦'
        lowest_high_card = '5♠ 10♣ 8♣ 7♠ Q♦'
        self._assert_winner(0, [highest_high_card, lowest_high_card])

    def _assert_winner(self, winner_index, hand):
        hand = [hand_string_to_hand_mapper(card) for card in hand]
        winnerIndex = HandMatcher().compare(hand)
        self.assertEqual(winner_index, winner_index)
