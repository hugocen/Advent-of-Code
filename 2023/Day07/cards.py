class Hand:
    def __init__(self, cards, bet, part2=False):
        self.cards = cards
        self.bet = bet
        self.rank = 0
        self.power = 0
        if part2:
            if 0 in self.cards:
                self.power = self.get_possible_max_power()
            else:
                self.power = self.get_power()
        else:
            self.power = self.get_power()

    def new_hand_with_joker(self, joker):
        cards = self.cards.copy()
        for i in range(5):
            if cards[i] == 0:
                cards[i] = joker
        return Hand(cards, self.bet)

    def get_possible_max_power(self):
        cards = self.get_possible_cards()
        cards.sort(reverse=True)
        return cards[0].power

    def get_possible_cards(self):
        possible_cards = []
        for i in range(1, 15):
            card = self.new_hand_with_joker(i)
            possible_cards.append(card)

        return possible_cards

    def get_power(self):
        if self.is_five_of_a_kind():
            return 7
        elif self.is_four_of_a_kind():
            return 6
        elif self.is_full_house():
            return 5
        elif self.is_three_of_a_kind():
            return 4
        elif self.is_two_pairs():
            return 3
        elif self.is_one_pair():
            return 2
        else:
            return 1

    def __repr__(self):
        return f"{self.cards} {self.bet} {self.power}"

    def is_five_of_a_kind(self):
        return len(set(self.cards)) == 1

    def is_four_of_a_kind(self):
        return len(set(self.cards)) == 2 and self.cards.count(self.cards[0]) in [1, 4]

    def is_full_house(self):
        return len(set(self.cards)) == 2 and self.cards.count(self.cards[0]) in [2, 3]

    def is_three_of_a_kind(self):
        if len(set(self.cards)) != 3:
            return False
        for card in self.cards:
            if self.cards.count(card) == 3:
                return True
        return False

    def is_two_pairs(self):
        return len(set(self.cards)) == 3 and self.cards.count(self.cards[0]) in [1, 2]

    def is_one_pair(self):
        return len(set(self.cards)) == 4 and self.cards.count(self.cards[0]) in [1, 2]

    def compare_same_power(self, other):
        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue
            return self_card > other_card
        return False

    def __lt__(self, other):
        if self.power == other.power:
            return not self.compare_same_power(other)
        return self.power < other.power

    def __gt__(self, other):
        if self.power == other.power:
            return self.compare_same_power(other)
        return self.power > other.power

    def __eq__(self, other):
        if self.power == other.power:
            return not self.compare_same_power(other)
        return self.power == other.power

    def __ne__(self, other):
        if self.power == other.power:
            return self.compare_same_power(other)
        return self.power != other.power

    def __le__(self, other):
        if self.power == other.power:
            return not self.compare_same_power(other)
        return self.power <= other.power

    def __ge__(self, other):
        if self.power == other.power:
            return self.compare_same_power(other)
        return self.power >= other.power
