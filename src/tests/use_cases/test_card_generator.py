import unittest

from use_cases.card_generator import generate_distinct_high_cards, generate_all_distinct_combinations, generate_straights, generate_four_of_a_kind, generate_full_houses, generate_three_of_a_kind, generate_two_pairs, generate_one_pairs

DISTINCT_POSIBILITIES = {
    'STRAIGHT_FLUSH': 10,
    'FOUR_OF_A_KIND': 156,
    'FULL_HOUSES': 156,
    'FLUSH': 1277,  # same then high_card but with same suit
    'STRAIGHT': 10,
    'THREE_OF_A_KIND': 858,
    'TWO_PAIR': 858,
    'ONE_PAIR': 2860,
    'HIGH_CARD': 1277
}


class TestCardGeneration(unittest.TestCase):

    def test_generate_all_combinations(self):
        actual = len(generate_all_distinct_combinations())
        expected = sum(list(DISTINCT_POSIBILITIES.values()))
        self.assertEqual(actual, expected)

    def test_that_all_straights_are_generated(self):
        actual = len(generate_straights())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['STRAIGHT'])

    def test_that_all_four_of_a_kind_are_generated(self):
        actual = len(generate_four_of_a_kind())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['FOUR_OF_A_KIND'])

    def test_that_all_full_houses_are_generated(self):
        actual = len(generate_full_houses())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['FULL_HOUSES'])

    def test_that_all_three_of_a_kind_are_generated(self):
        actual = len(generate_three_of_a_kind())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['THREE_OF_A_KIND'])

    def test_that_all_two_pairs_are_generated(self):
        actual = len(generate_two_pairs())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['TWO_PAIR'])

    def test_that_all_one_pairs_are_generated(self):
        actual = len(generate_one_pairs())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['ONE_PAIR'])

    def test_that_all_high_cards_are_generated(self):
        actual = len(generate_distinct_high_cards())
        self.assertEqual(actual,
                         DISTINCT_POSIBILITIES['HIGH_CARD'])
