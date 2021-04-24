from collections import Counter

from src.entities.deck import Card, Suit, Pip
from src.entities.hand import Hand


class HandParser:

    def parse(self, hand: [Card]):

        self._hand = hand
        self._ordered_hand = None
        self._card_pips = None
        self._card_suits = None
        self._pip_counter = None
        self._suit_counter = None

        hand_type = self._detect_royal_flush() or \
            self._detect_straight_flush() or \
            self._detect_four_of_a_kind() or \
            self._detect_full_house() or \
            self._detect_flush() or \
            self._detect_straight() or \
            self._detect_three_of_a_kind() or \
            self._detect_two_pair() or \
            self._detect_one_pair()

        return hand_type or Hand.HighCard

    def _detect_royal_flush(self):
        if self._check_integer_ascending_sequence(self.card_pips, start=10):
            if self._detect_flush():
                return Hand.RoyalFlush

    def _detect_straight_flush(self):
        if self._check_integer_ascending_sequence(self.card_pips):
            if self._detect_flush():
                return Hand.StraightFlush

    def _detect_four_of_a_kind(self):
        ocurrences = self.pip_counter.values()
        if 4 in ocurrences and 1 in ocurrences:
            return Hand.FourOfAKind

    def _detect_full_house(self):
        ocurrences = self.pip_counter.values()
        if 3 in ocurrences and 2 in ocurrences:
            return Hand.FullHouse

    def _detect_flush(self):
        if 5 in self.suit_counter.values():
            return Hand.Flush

    def _detect_straight(self):
        if self._check_integer_ascending_sequence(self.card_pips):
            return Hand.Straight

    def _detect_three_of_a_kind(self):
        if 3 in self.pip_counter.values():
            return Hand.ThreeOfAKind

    def _detect_two_pair(self):
        ocurrences = self.pip_counter.values()
        pairs = 0
        for n in ocurrences:
            if n == 2:
                pairs = pairs + 1
        return Hand.TwoPair if pairs == 2 else None

    def _detect_one_pair(self):
        if 2 in self.pip_counter.values():
            return Hand.OnePair

    @property
    def ordered_hand(self):
        if self._ordered_hand is None:
            self._ordered_hand = self._hand
            self._hand.sort(key=lambda x: x.pip.value)
        return self._ordered_hand

    @property
    def card_pips(self):
        if self._card_pips is None:
            self._card_pips = [card.pip.value for card in self.ordered_hand]
        return self._card_pips

    @property
    def pip_counter(self):
        if self._pip_counter is None:
            self._pip_counter = Counter(self.card_pips)
        return self._pip_counter

    @property
    def card_suits(self):
        if self._card_suits is None:
            self._card_suits = [card.suit.value for card in self.ordered_hand]
        return self._card_suits

    @property
    def suit_counter(self):
        if self._suit_counter is None:
            self._suit_counter = Counter(self.card_suits)
        return self._suit_counter

    def _check_integer_ascending_sequence(self, array, *, start=None):
        start = start or array[0]
        normalized_array = [array[i] - start - i for i in range(len(array))]
        return Counter(normalized_array)[0] == 5
