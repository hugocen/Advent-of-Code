# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
# pylint: disable=missing-class-docstring,missing-function-docstring
import re
import copy


class Day05(Base):
    stacks = []
    origin_stack = []
    moves = []

    def get_crates(self, line):
        for i in range(1, len(line), 4):
            idx = (i - 1) // 4
            if line[i] != " " and line[i].isalpha():
                self.stacks[idx] = [line[i]] + self.stacks[idx]

    def get_moves(self, line):
        pattern = r"move (\d+) from (\d+) to (\d+)"
        regex = re.compile(pattern)
        result = regex.search(line)
        if result:
            self.moves.append([int(result.group(1)), int(result.group(2)), int(result.group(3))])

    def preprocess_data(self):
        self.stacks = [[] for _ in range((len(self.data[0]) + 1) // 4)]
        in_stack = True
        for line in self.data:
            if in_stack:
                self.get_crates(line)
            else:
                self.get_moves(line)
            if line == "":
                in_stack = False
        self.origin_stack = copy.deepcopy(self.stacks)

    def puzzle1(self):
        for move in self.moves:
            for _ in range(move[0]):
                crate = self.stacks[move[1]-1].pop()
                self.stacks[move[2]-1].append(crate)
        
        result = ""
        for stack in self.stacks:
            result += stack[-1]

        print(f"Crates on top of each stack: {result}")
        self.stacks = self.origin_stack

    def puzzle2(self):
        for move in self.moves:
            crates = self.stacks[move[1]-1][-1 * move[0]:]
            self.stacks[move[1]-1] = self.stacks[move[1]-1][:-1 * move[0]:]
            self.stacks[move[2]-1] += crates
        
        result = ""
        for stack in self.stacks:
            result += stack[-1]

        print(f"Crates on top of each stack: {result}")


if __name__ == "__main__":
    obj = Day05()
    obj.run()
