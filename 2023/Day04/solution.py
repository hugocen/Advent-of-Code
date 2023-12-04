from unittest import result


class Solution:
    def parse_data(self, data):
        cards = []
        for line in data:
            all_numbers = line.split(": ")[1]
            wining_number = set(all_numbers.split(" | ")[0].split(" "))
            my_number = all_numbers.split(" | ")[1].split(" ")
            my_number = [number for number in my_number if number]
            cards.append((wining_number, my_number))
        return cards

    def get_score(self, card):
        score = 0
        for number in card[1]:
            if number in card[0]:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        return score

    def get_matching_numbers(self, card):
        return len(card[0].intersection(set(card[1])))

    def go_through_cards(self, cards, idx):
        if idx > len(cards) - 1:
            return 0
        if idx in self.dp:
            return self.dp[idx]
        result = 1
        matching_numbers = self.get_matching_numbers(cards[idx])
        for i in range(idx + 1, idx + matching_numbers + 1):
            result += self.go_through_cards(cards, i)
        self.dp[idx] = result
        return result

    def question_1(self, data):
        cards = self.parse_data(data)
        result = 0
        for wining_number, my_number in cards:
            result += self.get_score((wining_number, my_number))
        return result

    def question_2(self, data):
        self.dp = {}
        cards = self.parse_data(data)
        result = 0
        for i in range(len(cards)):
            result += self.go_through_cards(cards, i)
        return result
