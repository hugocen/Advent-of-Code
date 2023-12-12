import sys
import unittest
import os
from unittest import result

sys.path.append("../")
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_parse_data(self):
        pass

    def test_get_record(self):
        test_data = "???.### 1,1,3"
        expected = ("???.###", [1, 1, 3])
        self.assertEqual(self.solution.get_record(test_data), expected)

    def test_count_springs(self):
        test_data = "#.#.###"
        expected = [1, 1, 3]
        self.assertEqual(self.solution.count_springs(test_data), expected)
        test_data = ".#...#....###"
        expected = [1, 1, 3]
        self.assertEqual(self.solution.count_springs(test_data), expected)
        test_data = ".#.###.#.######"
        expected = [1, 3, 1, 6]
        self.assertEqual(self.solution.count_springs(test_data), expected)
        test_data = "####.#...#..."
        expected = [4, 1, 1]
        self.assertEqual(self.solution.count_springs(test_data), expected)
        test_data = "#....######..#####."
        expected = [1, 6, 5]
        self.assertEqual(self.solution.count_springs(test_data), expected)
        test_data = ".###.##....#"
        expected = [3, 2, 1]
        self.assertEqual(self.solution.count_springs(test_data), expected)

    # def test_guess(self):
    #     test_data = (["?", "?", "?", ".", "#", "#", "#"], [1, 1, 3])
    #     self.assertEqual(self.solution.guess(test_data[0], test_data[1], sum(test_data[1]), {}), 1)
    #     test_data = (["?", "?", "?", ".", "#", "#", "#"], [1, 1, 2])
    #     self.assertEqual(self.solution.guess(test_data[0], test_data[1], sum(test_data[1]), {}), 0)
    #     test_data = (
    #         [".", "?", "?", ".", ".", "?", "?", ".", ".", ".", "?", "#", "#", "."],
    #         [1, 1, 3],
    #     )
    #     self.assertEqual(self.solution.guess(test_data[0], test_data[1], sum(test_data[1]), {}), 4)

    def test_question_1_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        self.assertEqual(result, 21)

    # def test_question_1(self):
    #     sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    #     with open(sample_file_path, "r") as f:
    #         data = f.read()
    #     result = self.solution.question_1(data)
    #     print(f"Question 1: {result}")

    def test_get_record2(self):
        test_data = ".# 1"
        expected = ".#?.#?.#?.#?.# 1,1,1,1,1"
        self.assertEqual(self.solution.get_record2(test_data), expected)
        test_data = "???.### 1,1,3"
        expected = "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
        self.assertEqual(self.solution.get_record2(test_data), expected)

    def test_question_2_sample(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        self.assertEqual(self.solution.question_2(data), 525152)

    # def test_question_2(self):
    #     sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    #     with open(sample_file_path, "r") as f:
    #         data = f.read()
    #     result = self.solution.question_2(data)
    #     print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
