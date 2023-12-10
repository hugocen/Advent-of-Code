import sys
import unittest
import os

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_data(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        times, distances = self.solution.parse_data(data)
        assert times == [7, 15, 30]
        assert distances == [9, 40, 200]

    def test_parse_data2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        times, distances = self.solution.parse_data2(data)
        assert times == 71530
        assert distances == 940200

    def test_get_possible_win(self):
        assert self.solution.get_possible_win(7, 9) == 4
        assert self.solution.get_possible_win(15, 40) == 8
        assert self.solution.get_possible_win(30, 200) == 9

    def test_get_possible_win2(self):
        assert self.solution.get_possible_win2(7, 9) == 4
        assert self.solution.get_possible_win2(15, 40) == 8
        assert self.solution.get_possible_win2(30, 200) == 9
        assert self.solution.get_possible_win2(71530, 940200) == 71503

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        assert self.solution.question_1(data) == 288

    def test_question_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        print(f"Question 1: {self.solution.question_1(data)}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        assert self.solution.question_2(data) == 71503

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        print(f"Question 2: {self.solution.question_2(data)}")


if __name__ == "__main__":
    unittest.main()
