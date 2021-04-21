from src.entities.deck import Deck, Card
from src.entities.hand import Hand


class HandDetector:
    def detect_hand(self, hand: [Card]):
        hand_type = self._detect_royal_flush(hand) or \
            self._detect_straight_flush(hand) or \
            self._detect_four_of_a_kind(hand) or \
            self._detect_full_house(hand) or \
            self._detect_flush(hand) or \
            self._detect_straight(hand) or \
            self._detect_three_of_a_kind(hand) or \
            self._detect_two_pair(hand) or \
            self._detect_one_pair(hand)
        return hand_type or Hand.HighCard

    def _detect_royal_flush(self, hand: [Card]):
        ordered_hand = hand.sort(key=lambda x: x.number)
        card_numbers = [card.number for card in hand]
        if card_numbers[0] == 0 and self._check_integer_ascending_sequence(card_numbers[1:]):
            if self._detect_flush(hand):
                return Hand.RoyalFlush

    def _detect_straight_flush(self, hand: [Card]):
        ordered_hand = hand.sort(key=lambda x: x.number)
        card_numbers = [card.number for card in hand]
        if self._check_integer_ascending_sequence(card_numbers):
            if self._detect_flush(hand):
                return Hand.StraightFlush

    def _detect_four_of_a_kind(self, hand: [Card]):
        card_numbers = [card.number for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(card_numbers)

        if len(number_ocurrences.keys()) != 2:
            return None

        n1, n2 = number_ocurrences.keys()
        if number_ocurrences[n1] == 4 and number_ocurrences[n2] == 1 or \
                number_ocurrences[n1] == 1 and number_ocurrences[n2] == 4:
            return Hand.FourOfAKind

    def _detect_full_house(self, hand: [Card]):
        card_numbers = [card.number for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(card_numbers)
        if len(number_ocurrences.keys()) != 2:
            return None
        n1, n2 = number_ocurrences.keys()
        if number_ocurrences[n1] == 3 and number_ocurrences[n2] == 2 or \
                number_ocurrences[n1] == 2 and number_ocurrences[n2] == 3:
            return Hand.FullHouse

    def _detect_flush(self, hand: [Card]):
        suits = [card.suit for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(suits)
        if list(number_ocurrences.values())[0] == 5:
            return Hand.Flush

    def _detect_straight(self, hand: [Card]):
        ordered_hand = hand.sort(key=lambda x: x.number)
        card_numbers = [card.number for card in hand]
        if self._check_integer_ascending_sequence(card_numbers):
            return Hand.Straight

    def _detect_three_of_a_kind(self, hand: [Card]):
        card_numbers = [card.number for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(card_numbers)
        for x in number_ocurrences.values():
            if x == 3:
                return Hand.ThreeOfAKind

    def _detect_two_pair(self, hand: [Card]):
        card_numbers = [card.number for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(card_numbers)
        pairs = 0
        for x in number_ocurrences.values():
            if x == 2:
                pairs = pairs + 1
            if pairs == 2:
                return Hand.TwoPair

    def _detect_one_pair(self, hand: [Card]):
        card_numbers = [card.number for card in hand]
        number_ocurrences = self._count_ocurrences_in_list(card_numbers)
        for x in number_ocurrences.values():
            if x == 2:
                return Hand.OnePair

    def _count_ocurrences_in_list(self, l):
        ocurrences = {}
        for i in l:
            ocurrences[i] = ocurrences.get(i, 0) + 1
        return ocurrences

    def _check_integer_ascending_sequence(self, array):
        normalized_array = [array[i] - array[0] - i for i in range(len(array))]
        return len(set(normalized_array)) == 1
