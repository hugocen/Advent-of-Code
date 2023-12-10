import sys
import unittest
import os

sys.path.append("../")
from solution import Solution
from cards import Hand


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_cards(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        hands = self.solution.parse_data(data)
        assert hands[0].cards == [3, 2, 10, 3, 13]
        assert hands[0].bet == 765
        assert hands[1].cards == [10, 5, 5, 11, 5]
        assert hands[1].bet == 684
        assert hands[2].cards == [13, 13, 6, 7, 7]
        assert hands[2].bet == 28
        assert hands[3].cards == [13, 10, 11, 11, 10]
        assert hands[3].bet == 220
        assert hands[4].cards == [12, 12, 12, 11, 14]
        assert hands[4].bet == 483

    def test_is_five_of_a_kind(self):
        hand = Hand([3, 3, 3, 3, 3], 1)
        assert hand.is_five_of_a_kind() == True
        hand = Hand([3, 3, 3, 3, 4], 1)
        assert hand.is_five_of_a_kind() == False

    def test_is_four_of_a_kind(self):
        hand = Hand([3, 3, 3, 3, 4], 1)
        assert hand.is_four_of_a_kind() == True
        hand = Hand([3, 3, 3, 4, 4], 1)
        assert hand.is_four_of_a_kind() == False

    def test_is_full_house(self):
        hand = Hand([3, 3, 3, 4, 4], 1)
        assert hand.is_full_house() == True
        hand = Hand([3, 3, 4, 4, 4], 1)
        assert hand.is_full_house() == True
        hand = Hand([3, 3, 3, 4, 5], 1)
        assert hand.is_full_house() == False

    def test_is_three_of_a_kind(self):
        hand = Hand([3, 3, 3, 4, 5], 1)
        assert hand.is_three_of_a_kind() == True
        hand = Hand([3, 3, 4, 4, 5], 1)
        assert hand.is_three_of_a_kind() == False
        hand = Hand([13, 10, 11, 11, 10], 1)
        assert hand.is_three_of_a_kind() == False

    def test_is_two_pairs(self):
        hand = Hand([3, 3, 4, 4, 5], 1)
        assert hand.is_two_pairs() == True
        hand = Hand([3, 3, 3, 4, 5], 1)
        assert hand.is_two_pairs() == False

    def test_is_one_pair(self):
        hand = Hand([3, 3, 4, 5, 6], 1)
        assert hand.is_one_pair() == True
        hand = Hand([3, 4, 5, 6, 7], 1)
        assert hand.is_one_pair() == False

    def test_get_power(self):
        hand = Hand([3, 3, 4, 5, 6], 1)
        assert hand.power == 2
        hand = Hand([3, 3, 4, 4, 6], 1)
        assert hand.power == 3
        hand = Hand([3, 3, 3, 4, 6], 1)
        assert hand.power == 4
        hand = Hand([3, 3, 3, 4, 4], 1)
        assert hand.power == 5
        hand = Hand([3, 3, 3, 3, 4], 1)
        assert hand.power == 6
        hand = Hand([3, 3, 3, 3, 3], 1)
        assert hand.power == 7

    def test_compare_same_power(self):
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 4, 5, 7], 1)
        assert hand1.compare_same_power(hand2) == False
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 4, 5, 5], 1)
        assert hand1.compare_same_power(hand2) == True

    def test_lt(self):
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 3, 3, 7], 1)
        assert (hand1 < hand2) == True
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 4, 5, 2], 1)
        assert (hand1 < hand2) == False

    def test_gt(self):
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 4, 5, 7], 1)
        assert (hand1 > hand2) == False
        hand1 = Hand([3, 3, 4, 5, 6], 1)
        hand2 = Hand([3, 3, 4, 5, 2], 1)
        assert (hand1 > hand2) == True

    def test_get_possible_max_power(self):
        hand = Hand([13, 10, 0, 0, 10], 1)
        assert hand.get_possible_max_power() == 6
        hand = Hand([13, 5, 0, 0, 10], 2)
        assert hand.get_possible_max_power() == 4
        hand = Hand([13, 13, 0, 10, 10], 3)
        assert hand.get_possible_max_power() == 5

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 6440

    def test_question_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        print(f"Question 1: {result}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        assert result == 5905

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
