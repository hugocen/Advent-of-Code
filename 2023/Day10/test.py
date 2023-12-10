import sys
import unittest
import os

sys.path.append("../")
from solution import Solution
from pipe import Pipe


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_starting_nodes(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_1.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        pipes = self.solution.parse_data(data)
        starting_point = self.solution.get_starting_point(pipes)
        assert starting_point.x == 1
        assert starting_point.y == 1
        assert starting_point.shape == "S"

        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_2.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()

        pipes = self.solution.parse_data(data)
        starting_point = self.solution.get_starting_point(pipes)
        assert starting_point.x == 0
        assert starting_point.y == 2
        assert starting_point.shape == "S"

    def test_pipe_next(self):
        test_pipe = Pipe(1, 2, "|")
        next_point = test_pipe.next(1, 1)
        assert next_point == (1, 3)
        test_pipe = Pipe(1, 2, "|")
        next_point = test_pipe.next(1, 3)
        assert next_point == (1, 1)

        test_pipe = Pipe(1, 2, "-")
        next_point = test_pipe.next(0, 2)
        assert next_point == (2, 2)
        test_pipe = Pipe(1, 2, "-")
        next_point = test_pipe.next(2, 2)
        assert next_point == (0, 2)

        test_pipe = Pipe(1, 2, "L")
        next_point = test_pipe.next(1, 1)
        assert next_point == (2, 2)
        test_pipe = Pipe(1, 2, "L")
        next_point = test_pipe.next(2, 2)
        assert next_point == (1, 1)

        test_pipe = Pipe(1, 2, "J")
        next_point = test_pipe.next(1, 1)
        assert next_point == (0, 2)
        test_pipe = Pipe(1, 2, "J")
        next_point = test_pipe.next(0, 2)
        assert next_point == (1, 1)

        test_pipe = Pipe(1, 2, "7")
        next_point = test_pipe.next(1, 1)
        assert next_point == (0, 2)
        test_pipe = Pipe(1, 2, "7")
        next_point = test_pipe.next(0, 2)
        assert next_point == (1, 3)

        test_pipe = Pipe(1, 2, "F")
        next_point = test_pipe.next(1, 3)
        assert next_point == (2, 2)
        test_pipe = Pipe(1, 2, "F")
        next_point = test_pipe.next(2, 2)
        assert next_point == (1, 3)

        test_pipe = Pipe(1, 2, "S")
        next_point = test_pipe.next(1, 3)
        assert next_point == (1, 2)

        test_pipe = Pipe(1, 2, ".")
        next_point = test_pipe.next(1, 3)
        assert next_point is None

    def test_get_possible_routes(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_1.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        pipes = self.solution.parse_data(data)
        starting_point = self.solution.get_starting_point(pipes)
        routes = self.solution.get_possible_routes(pipes, starting_point)
        assert routes == [(2, 1), (1, 2)]

        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_2.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        pipes = self.solution.parse_data(data)
        starting_point = self.solution.get_starting_point(pipes)
        routes = self.solution.get_possible_routes(pipes, starting_point)
        assert routes == [(1, 2), (0, 3)]

    def test_question_1_sample_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_1.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 4

    def test_question_1_sample_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_2.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        assert result == 8

    def test_question_1(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_1(data)
        print(f"Question 1: {result}")

    def test_question_2_sample_3(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_3.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"test_question_2_sample_3: {result}")
        assert result == 4

    def test_question_2_sample_4(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_4.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"test_question_2_sample_4: {result}")
        assert result == 8

    def test_question_2_sample_5(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_5.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"test_question_2_sample_5: {result}")
        assert result == 10

    def test_question_2_sample_6(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample_6.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"test_question_2_sample_6: {result}")
        assert result == 4

    def test_question_2(self):
        sample_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(sample_file_path, "r") as f:
            data = f.read()
        result = self.solution.question_2(data)
        print(f"Question 2: {result}")


if __name__ == "__main__":
    unittest.main()
