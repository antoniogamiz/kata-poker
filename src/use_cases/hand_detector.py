from src.entities.deck import Deck, Card
from src.entities.hand import Hand


class HandDetector:
    def detect_hand(self, hand: [Card]):
        hand_type = self._detect_royal_flush(hand)
        return hand_type or Hand.Empty

    def _detect_royal_flush(self, hand: [Card]):
        ordered_hand = hand.sort(key=lambda x: x.number)
        cards_ids = [card.number for card in hand]
        if cards_ids[0] == 0 and self._check_integer_ascending_sequence(cards_ids[1:]) or self._check_integer_ascending_sequence(cards_ids):
            return Hand.RoyalFlush

        return None

    def _check_integer_ascending_sequence(self, array):
        normalized_array = [array[i] - array[0] - i for i in range(len(array))]
        return len(set(normalized_array)) == 1
