from entities.deck import Card, Suit, Pip


unicode_to_suit_map = {
    '♠': Suit.SPADES,
    '♥': Suit.HEARTS,
    '♦': Suit.DIAMONDS,
    '♣': Suit.CLUBS
}

string_to_pip_map = {
    'A': Pip.ACE,
    '2':  Pip.TWO,
    '3':  Pip.THREE,
    '4':  Pip.FOUR,
    '5':  Pip.FIVE,
    '6':  Pip.SIX,
    '7':  Pip.SEVEN,
    '8':  Pip.EIGHT,
    '9':  Pip.NINE,
    '10':  Pip.TEN,
    'J': Pip.J,
    'Q': Pip.Q,
    'K': Pip.K
}


def string_to_card_mapper(string):
    pip_string = string[0:-1]
    pip = string_to_pip_map[pip_string]

    suit_string = string[-1]
    suit = unicode_to_suit_map[suit_string]

    return Card(suit, pip)


def hand_string_to_hand_mapper(string):
    card_strings = string.split(" ")
    return [string_to_card_mapper(card_string) for card_string in card_strings]
