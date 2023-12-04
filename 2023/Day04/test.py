import sys
import unittest
import os

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_data(self):
        test_data = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        ]
        expected = [
            (
                {"41", "48", "83", "86", "17"},
                ["83", "86", "6", "31", "17", "9", "48", "53"],
            ),
            (
                {"13", "32", "20", "16", "61"},
                ["61", "30", "68", "82", "17", "32", "24", "19"],
            ),
        ]
        output = self.solution.parse_data(test_data)
        print(output)
        assert output == expected

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_1(data)
            assert output == 13

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
            print(output)
            assert output == 30

    def test_question_2(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read().splitlines()
            output = self.solution.question_2(data)
            print(f"Question 2: {output}")


if __name__ == "__main__":
    unittest.main()
