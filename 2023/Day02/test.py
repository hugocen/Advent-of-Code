from calendar import c
import sys
import unittest
import os

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read().splitlines()
            assert self.solution.question_1(data) == 8

    def test_question_1(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read().splitlines()
            print(f"Question 1: {self.solution.question_1(data)}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read().splitlines()
            assert self.solution.question_2(data) == 2286

    def test_question_2(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read().splitlines()
            print(f"Question 2: {self.solution.question_2(data)}")


if __name__ == "__main__":
    unittest.main()
