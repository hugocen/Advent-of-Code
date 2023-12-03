import re
import sys
import unittest
import os
from unittest import result

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_numbers(self):
        data = [
            ".....+.58.",
            "..592.....",
            "........21",
        ]
        expected = [
            (58, {(7, 0), (8, 0)}),
            (592, {(2, 1), (3, 1), (4, 1)}),
            (21, {(8, 2), (9, 2)}),
        ]
        output = self.solution.get_numbers(data)
        assert output == expected

    def test_get_engine_parts(self):
        data = [
            "..#",
            "#9.",
            "../",
        ]
        expected = [
            ("#", 2, 0),
            ("#", 0, 1),
            ("/", 2, 2),
        ]
        output = self.solution.get_engine_parts(data)
        assert output == expected

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_1(data)
            assert output == 4361

    def test_question_1(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_1(data)
            print(f"Question 1: {output}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_2(data)
            assert output == 467835

    def test_question_2(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_2(data)
            print(f"Question 2: {output}")


if __name__ == "__main__":
    unittest.main()
