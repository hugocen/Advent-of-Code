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

        expected_data = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]

        result = self.solution.parse_data(data)
        assert result == expected_data

    def test_find_differences(self):
        history = [[0, 3, 6, 9, 12, 15]]
        expected_history = [
            [0, 3, 6, 9, 12, 15],
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ]
        result = self.solution.find_differences(history)
        print(result)
        assert result == expected_history

    def test_find_extrapolated_numbers(self):
        history = [
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ]
        expected_history = [
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ]
        self.solution.find_extrapolated_numbers(history, 0)
        assert history == expected_history

    def test_find_all_extrapolated_numbers(self):
        history = [[0, 3, 6, 9, 12, 15]]
        history = self.solution.find_differences(history)
        expected_history = [
            [0, 3, 6, 9, 12, 15, 18],
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0],
        ]
        self.solution.find_all_extrapolated_numbers(history)
        assert history == expected_history


    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 114

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
        assert result == 2

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
