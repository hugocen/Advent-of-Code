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

        expanded_sample_file_path = os.path.join(
            os.path.dirname(__file__), "sample_expanded.txt"
        )
        with open(expanded_sample_file_path, "r") as f:
            expanded_data = f.read()
        space = self.solution.parse_data(data)

        expanded_data = expanded_data.splitlines()
        for y, row in enumerate(expanded_data):
            expanded_data[y] = list(row)

        self.assertEqual(space, expanded_data)

    def test_get_galaxies(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        space = self.solution.parse_data(data)
        galaxies = self.solution.get_galaxies(space)
        self.assertEqual(
            galaxies,
            [
                (4, 0),
                (9, 1),
                (0, 2),
                (8, 5),
                (1, 6),
                (12, 7),
                (9, 10),
                (0, 11),
                (5, 11),
            ],
        )

    def test_get_distance(self):
        a = (1, 6)
        b = (5, 11)
        self.assertEqual(self.solution.get_distance(a, b), 9)
        a = (4, 0)
        b = (9, 10)
        self.assertEqual(self.solution.get_distance(a, b), 15)
        a = (0, 2)
        b = (12, 7)
        self.assertEqual(self.solution.get_distance(a, b), 17)
        a = (0, 11)
        b = (5, 11)
        self.assertEqual(self.solution.get_distance(a, b), 5)

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        self.assertEqual(result, 374)

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
        self.assertEqual(self.solution.question_2(data, 10), 1030)
        self.assertEqual(self.solution.question_2(data, 100), 8410)

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
