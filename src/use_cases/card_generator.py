from itertools import combinations
from collections import Counter

from copy import copy
from entities.deck import Suit, Pip

CARDS_IN_HAND = 5


def generate_all_distinct_combinations():
    straight_flush = generate_straights()
    four_of_a_kind = generate_four_of_a_kind()
    full_houses = generate_full_houses()
    flush = generate_distinct_high_cards()
    straight = generate_straights()
    three_of_a_kind = generate_three_of_a_kind()
    two_pair = generate_two_pairs()
    one_pair = generate_one_pairs()
    high_cards = flush
    all_combinations = straight_flush + four_of_a_kind + \
        full_houses + flush + straight + three_of_a_kind + \
        two_pair + one_pair + high_cards
    return _map_combinations_to_pips(all_combinations)


def _map_combinations_to_pips(combinations):
    return list(map(lambda values: [list(Pip)[x].value for x in values], combinations))


def generate_straights():
    first_straight = [0, 1, 2, 3, 4]
    straights = []
    for i in range(9):
        straights.append(map(lambda x: x+i, first_straight))
    straights.reverse()
    return [_create_highest_straight()] + straights


def _create_highest_straight():
    return [0, 9, 10, 11, 12]


def generate_four_of_a_kind():
    numbers = range(13)
    four_of_a_kind = []
    for i in numbers:
        for j in numbers:
            if i != j:
                four_of_a_kind.append([i]*4 + [j])
    return four_of_a_kind


def generate_full_houses():
    numbers = range(13)
    full_houses = []
    for i in numbers:
        for j in numbers:
            if i != j:
                full_houses.append([i]*3 + [j]*2)
    return full_houses


def generate_three_of_a_kind():
    numbers = list(range(13))
    three_of_a_kind = []
    for x in numbers:
        possible_other_cards = copy(numbers)
        possible_other_cards.remove(x)
        possibles_cards = list(combinations(possible_other_cards, 2))
        all_hands = list(map(lambda i: [x]*3+list(i), possibles_cards))
        three_of_a_kind += all_hands
    return three_of_a_kind


def generate_two_pairs():
    numbers = list(range(13))
    two_pairs = []
    visited = []
    for x in numbers:
        possible_other_cards = copy(numbers)
        possible_other_cards.remove(x)
        for y in range(x+1, len(numbers)):
            possible_other_cards.remove(y)
            all_hands = list(
                map(lambda i: [x]*2+[y]*2+[i], possible_other_cards))
            two_pairs += all_hands
            possible_other_cards.append(y)
    return two_pairs


def generate_one_pairs():
    numbers = list(range(13))
    three_of_a_kind = []
    for x in numbers:
        possible_other_cards = copy(numbers)
        possible_other_cards.remove(x)
        possibles_cards = list(combinations(possible_other_cards, 3))
        all_hands = list(map(lambda i: [x]*2+list(i), possibles_cards))
        three_of_a_kind += all_hands
    return three_of_a_kind


def generate_distinct_high_cards():
    cards = range(13)
    combinations_with_straights = combinations(cards, CARDS_IN_HAND)
    combinations_without_straights = filter(
        _filter_straights, combinations_with_straights)
    return list(combinations_without_straights)


def _filter_straights(array):
    normalized_array = [array[i] - array[0] - i for i in range(len(array))]
    if _is_straight_flush(array):
        return False
    return Counter(normalized_array)[0] != 5


def _is_straight_flush(array):
    if array == (0, 9, 10, 11, 12):
        return True
