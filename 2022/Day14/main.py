# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on


class Day14(Base):
    rocks = set()
    lowest = float("-inf")
    start = (500, 0)

    def preprocess_data(self):
        self.sand_loc = set()
        for line in self.data:
            locs = line.split(" -> ")
            wall = []
            for loc in locs:
                coordinate = loc.split(",")
                wall.append([int(coordinate[0]), int(coordinate[1])])

            for i in range(1, len(wall)):
                if wall[i - 1][0] == wall[i][0]:
                    coords = [wall[i - 1][1], wall[i][1]]
                    coords.sort()
                    for j in range(coords[0], coords[1] + 1):
                        self.rocks.add((wall[i][0], j))
                else:
                    coords = [wall[i - 1][0], wall[i][0]]
                    coords.sort()
                    for j in range(coords[0], coords[1] + 1):
                        self.rocks.add((j, wall[i][1]))
        for rock in self.rocks:
            self.lowest = max(self.lowest, rock[1])

        self.rocks = set(self.rocks)

    def reset_data(self):
        self.sand_loc = set()

    def sand_fall(self, point):
        if self.check_in_abyss(point):
            return True
        
        down = (point[0], point[1] + 1)
        left = (point[0] - 1, point[1] + 1)
        right = (point[0] + 1, point[1] + 1)

        if down not in self.rocks and down not in self.sand_loc:
            return self.sand_fall(down)
        elif left not in self.rocks and left not in self.sand_loc:
            return self.sand_fall(left)
        elif right not in self.rocks and right not in self.sand_loc:
            return self.sand_fall(right)
        else:
            self.sand_loc.add(point)
            return False

    def check_in_abyss(self, point):
        if point[1] >= self.lowest:
            self.sand_loc.add(point)
            return True
        else:
            return False

    def puzzle1(self):
        sands = 0
        while True:
            sands += 1
            if self.sand_fall(self.start):
                print(f"How many units of sand come to rest before sand starts flowing into the abyss below? {sands-1}")
                return

    def puzzle2(self):
        sands = 0
        self.lowest += 1
        while True:
            sands += 1
            self.sand_fall(self.start)
            if self.start in self.sand_loc:
                print(f"How many units of sand come to rest? {sands}")
                return


if __name__ == "__main__":
    obj = Day14()
    obj.run()
