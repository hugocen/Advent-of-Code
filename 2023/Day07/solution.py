import sys

sys.path.append("../")
from cards import Hand


class Solution:
    def parse_cards(self, line, part2=False):
        cards = []
        for card in line:
            if card == "A":
                cards.append(14)
            elif card == "K":
                cards.append(13)
            elif card == "Q":
                cards.append(12)
            elif card == "J":
                if part2:
                    cards.append(0)
                else:
                    cards.append(11)
            elif card == "T":
                cards.append(10)
            else:
                cards.append(int(card))

        return cards

    def parse_data(self, data, part2=False):
        hands = []
        for line in data.splitlines():
            line = line.split(" ")
            hand = Hand(self.parse_cards(line[0], part2), int(line[1]), part2)
            hands.append(hand)
        return hands

    def question_1(self, data):
        hands = self.parse_data(data)
        hands.sort()
        result = 0
        for idx, hand in enumerate(hands):
            result += hand.bet * (idx + 1)
        return result

    def question_2(self, data):
        hands = self.parse_data(data, True)
        hands.sort()
        result = 0
        for idx, hand in enumerate(hands):
            result += hand.bet * (idx + 1)
        return result
