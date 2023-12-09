from random import sample
import sys
import unittest
import os

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_seeds(self):
        test_data = "Seeds: 1 2 3 4 5 6 7 8 9 10"
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output = self.solution.get_seeds(test_data)
        assert output == expected

    def test_get_seeds2(self):
        test_data = "Seeds: 5 3 10 2"
        expected = [(5, 3), (10, 2)]
        output = self.solution.get_seeds2(test_data)
        assert output == expected

    def test_get_map(self):
        test_data = """\
seed-to-soil map:
50 98 2
52 50 3"""
        expected = [(50, 98, 2), (52, 50, 3)]
        output = self.solution.get_map(test_data)
        assert output == expected

    def test_reverse_check_map(self):
        test_data = [(50, 98, 2), (52, 50, 3)]
        test_value = [50, 51, 52, 53, 79]
        expected = [98, 99, 50, 51, 79]
        for i in range(len(test_value)):
            output = self.solution.reverse_check_map(test_value[i], test_data)
            assert output == expected[i]

    def test_check_map(self):
        test_data = [(50, 98, 2), (52, 50, 3)]
        test_value = [98, 99, 50, 51, 79]
        expected = [50, 51, 52, 53, 79]
        for i in range(len(test_value)):
            output = self.solution.check_map(test_value[i], test_data)
            assert output == expected[i]

    def test_check_seeds(self):
        test_data = [5, 6, 7, 10, 11]
        seeds = [(5, 3), (10, 2)]
        for data in test_data:
            output = self.solution.check_seeds(data, seeds)
            assert output == True
        test_data = [1, 2, 3, 4, 8, 9, 12]
        for data in test_data:
            output = self.solution.check_seeds(data, seeds)
            assert output == False

    def test_question_1_not_sort_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
            output = self.solution.question_1_not_sort(data)
            assert output == [82, 43, 86, 35]

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
            output = self.solution.question_1(data)
            assert output == 35

    def test_question_1(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read()
            output = self.solution.question_1(data)
            print(f"Question 1: {output}")

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
            output = self.solution.question_2(data)
            assert output == 46

    def test_question_2(self):
        input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(input_file_path, "r") as f:
            data = f.read()
            output = self.solution.question_2(data)
            print(f"Question 2: {output}")


if __name__ == "__main__":
    unittest.main()
