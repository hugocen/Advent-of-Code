import sys
import unittest
import os

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_question_1_sample_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_1.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 2

    def test_question_1_sample_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_2.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 6

    def test_question_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        print(f"Question 1: {result}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_3.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        assert result == 6

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
