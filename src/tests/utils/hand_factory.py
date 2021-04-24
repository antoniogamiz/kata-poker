from entities.deck import Card


class HandFactory:
    def create_royal_flush(self):
        return [Card(1, 0, 12),
                Card(1, 9, 8),
                Card(1, 10, 9),
                Card(1, 11, 10),
                Card(1, 12, 11)]

    def create_almost_royal_flush(self):
        return [Card(1, 0, 12),
                Card(1, 9, 8),
                Card(1, 10, 9),
                Card(1, 11, 10),
                Card(2, 12, 11)]

    def create_straight_flush(self):
        return [Card(1, 8, 7),
                Card(1, 9, 8),
                Card(1, 10, 9),
                Card(1, 11, 10),
                Card(1, 12, 11)]

    def create_lower_straight_flush(self):
        return [Card(1, 7, 6),
                Card(1, 8, 7),
                Card(1, 9, 8),
                Card(1, 10, 9),
                Card(1, 11, 10)]

    def create_unordered_royal_flush(self):
        return [Card(1, 0, 12),
                Card(1, 9, 8),
                Card(1, 11, 10),
                Card(1, 10, 9),
                Card(1, 12, 11)]

    def create_four_of_a_kind(self):
        return [Card(0, 1, 12),
                Card(1, 1, 0),
                Card(2, 1, 0),
                Card(3, 1, 0),
                Card(1, 2, 1)]

    def create_full_house(self):
        return [Card(0, 10, 9),
                Card(1, 10, 9),
                Card(2, 10, 9),
                Card(1, 11, 10),
                Card(2, 11, 10)]

    def create_flush(self):
        return [Card(0, 5, 4),
                Card(0, 2, 1),
                Card(0, 4, 3),
                Card(0, 11, 10),
                Card(0, 1, 0)]

    def create_straight(self):
        return [Card(0, 1, 0),
                Card(1, 2, 1),
                Card(2, 3, 2),
                Card(3, 4, 3),
                Card(0, 5, 4)]

    def create_three_of_a_kind(self):
        return [Card(0, 0, 12),
                Card(1, 0, 12),
                Card(2, 0, 12),
                Card(3, 11, 10),
                Card(0, 1, 0)]

    def create_two_pair(self):
        return [Card(0, 0, 12),
                Card(1, 0, 12),
                Card(2, 3, 2),
                Card(3, 3, 2),
                Card(0, 1, 0)]

    def create_one_pair(self):
        return [Card(0, 0, 12),
                Card(1, 0, 12),
                Card(2, 3, 2),
                Card(3, 11, 10),
                Card(0, 1, 0)]

    def create_high_card(self):
        return [Card(0, 0, 12),
                Card(1, 5, 4),
                Card(2, 3, 2),
                Card(3, 11, 10),
                Card(0, 1, 0)]
