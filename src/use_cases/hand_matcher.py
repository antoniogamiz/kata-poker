from collections import Counter
from bisect import insort

from entities.deck import Card, Pip
from entities.hand import Hand
from use_cases.hand_parser import HandParser


class HandMatcher:
    def compare(self, hands: [[Card]]):
        hand_types = self._parse_hands(hands)
        sorted_hand_types = self._sort_hands_by_highest_type(hand_types)
        highest_hand_types = self._get_highest_hand_types(sorted_hand_types)

        if len(highest_hand_types) == 1:
            return highest_hand_types[0]['hand_index']

        return self._decide_winner_when_same_hand_types(highest_hand_types)

    def _parse_hands(self, hands: [[Card]]):
        parser = HandParser()
        return [{'hand_index': i, 'type': parser.parse(hand), 'hand': hand} for i, hand in enumerate(hands)]

    def _sort_hands_by_highest_type(self, hand_types):
        return sorted(hand_types,
                      key=lambda x: x['type'].value, reverse=True)

    def _get_highest_hand_types(self, sorted_hand_types):
        highest_type = sorted_hand_types[0]['type'].value
        highest_hands = []
        for hand_type in sorted_hand_types:
            if hand_type['type'].value == highest_type:
                highest_hands.append(hand_type)
        return highest_hands

    def _decide_winner_when_same_hand_types(self, hands):
        hand_type = hands[0]['type']
        parsed_hands_values = []
        for hand in hands:
            hand_values = [card.pip.value for card in hand['hand']]
            parsed_hands_values.append(self._parse_hand_values(hand_values))
        return -1

    def _parse_hand_values(self, values):
        inversed_counter = self._inverse_counnter(Counter(values))
        return [keys for keys in list(inversed_counter.keys())]

    def _inverse_counnter(self, counter):
        inversed_counter = {}
        for k, n in counter.items():
            if n in inversed_counter:
                insort(inversed_counter[n], k)
            else:
                inversed_counter[n] = [k]
        return inversed_counter
