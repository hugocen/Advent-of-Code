import sys
from utils import io
import abc


class Base:
    def __init__(self):
        if len(sys.argv) < 2:
            raise Exception("no inputs")
        self.input_file_path = sys.argv[1]
        self.__get_data()

    def __get_data(self):
        lines = io.get_data(self.input_file_path)
        self.data = []
        for line in lines:
            self.data.append(line.replace("\n", ""))

    @abc.abstractmethod
    def preprocess_data(self):
        pass

    @abc.abstractmethod
    def reset_data(self):
        pass

    @abc.abstractmethod
    def puzzle1(self):
        print("Puzzle 1 solution no implemented.")

    @abc.abstractmethod
    def puzzle2(self):
        print("Puzzle 2 solution no implemented.")

    def run(self):
        self.preprocess_data()
        self.puzzle1()
        self.reset_data()
        self.puzzle2()
