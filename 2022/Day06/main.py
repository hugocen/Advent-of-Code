# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
# pylint: disable=missing-class-docstring,missing-function-docstring


class Day06(Base):
    @staticmethod
    def get_first_marker_after_character(line, num_char):
        characters_set = set()
        for i, _ in enumerate(line):
            # print(characters_set)
            if i >= num_char:
                characters = line[i-num_char:i]
                characters_set = set(characters)
                if len(characters_set) == num_char:
                    print(f"First marker after character: {i}")
                    return

    def puzzle1(self):
        print("Puzzle 1")
        for line in self.data:
            self.get_first_marker_after_character(line, 4)

    def puzzle2(self):
        print("Puzzle 2")
        for line in self.data:
            self.get_first_marker_after_character(line, 14)


if __name__ == "__main__":
    obj = Day06()
    obj.run()
