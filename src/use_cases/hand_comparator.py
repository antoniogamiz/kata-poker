from entities.deck import Card
from entities.hand import Hand
from use_cases.hand_parser import HandParer


class HandComparator:
    @classmethod
    def compare(cls, hands: [[Card]]):
        highest_hands_indexes = cls._select_highest_hand_type_indexes(hands)

        if len(highest_hands_indexes) == 1:
            return highest_hands_indexes[0]

        highest_hands = [hands[i] for i in highest_hands_indexes]
        highest_hands_values = list(
            map(cls._calculate_hand_value, highest_hands))
        highest_hand_index = highest_hands_values.index(
            max(highest_hands_values))
        return highest_hands_indexes[highest_hand_index]

    @classmethod
    def _select_highest_hand_type_indexes(cls, hands: [[Card]]):
        detected_hands = cls._detect_hands(hands)
        highest_hand_type = cls._find_highest_hand_type(detected_hands)
        return [
            i for i, val in enumerate(detected_hands) if val == highest_hand_type]

    @classmethod
    def _detect_hands(cls, hands: [[Card]]):
        hand_detector = HandDetector()
        return [hand_detector.detect_hand(hand) for hand in hands]

    @classmethod
    def _find_highest_hand_type(cls, hand_types: [Hand]):
        return max(hand_types)

    @classmethod
    def _calculate_hand_value(cls, hand: [Card]):
        return sum([card.value for card in hand])
