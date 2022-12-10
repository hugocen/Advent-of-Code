# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
# pylint: disable=missing-class-docstring,missing-function-docstring


class Day08(Base):
    grid = []

    def preprocess_data(self):
        for line in self.data:
            rows = [int(x) for x in line]
            self.grid.append(rows)

    def print_grid(self):
        for row in self.grid:
            print(row)

    def look_left(self, tree, row, col):
        sees = 0
        for j in range(col - 1, -1, -1):
            if self.grid[row][j] >= tree:
                sees += 1
                return False, sees
            else:
                sees += 1
        return True, sees

    def look_right(self, tree, row, col):
        sees = 0
        for j in range(col + 1, len(self.grid[row])):
            if self.grid[row][j] >= tree:
                sees += 1
                return False, sees
            else:
                sees += 1
        return True, sees

    def look_up(self, tree, row, col):
        sees = 0
        for i in range(row - 1, -1, -1):
            if self.grid[i][col] >= tree:
                sees += 1
                return False, sees
            else:
                sees += 1
        return True, sees

    def look_down(self, tree, row, col):
        sees = 0
        for i in range(row + 1, len(self.grid)):
            if self.grid[i][col] >= tree:
                sees += 1
                return False, sees
            else:
                sees += 1
        return True, sees

    def puzzle1(self):
        visible_pos = 0
        for i, row in enumerate(self.grid):
            for j, tree in enumerate(row):
                if i == 0 or j == 0 or i == len(self.grid) - 1 or j == len(row) - 1:
                    visible_pos += 1
                else:
                    left, _ = self.look_left(tree, i, j)
                    right, _ = self.look_right(tree, i, j)
                    up, _ = self.look_up(tree, i, j)
                    down, _ = self.look_down(tree, i, j)
                    if left or right or up or down:
                        visible_pos += 1
        print(f"How many trees are visible from outside the grid? {visible_pos}")

    def puzzle2(self):
        top_scenic_score = float("-inf")
        for i, row in enumerate(self.grid):
            for j, tree in enumerate(row):
                if i == 0 or j == 0 or i == len(self.grid) - 1 or j == len(row) - 1:
                    continue
                else:
                    _, left = self.look_left(tree, i, j)
                    _, right = self.look_right(tree, i, j)
                    _, up = self.look_up(tree, i, j)
                    _, down = self.look_down(tree, i, j)
                    scenic_score = left * right * up * down
                    top_scenic_score = max(top_scenic_score, scenic_score)

        print(f"What is the highest scenic score possible for any tree? {top_scenic_score}")


if __name__ == "__main__":
    obj = Day08()
    obj.run()
