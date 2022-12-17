# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
import re
from tqdm import tqdm


class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = int(x)
        self.y = int(y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.radius = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)
        self.edges = self.get_edges()

    def is_in_circle(self, x, y):
        return abs(x - self.x) + abs(y - self.y) <= self.radius

    def get_edges(self):
        points = set()
        # up to right
        point = (self.x, self.y + self.radius + 1)
        for i in range(self.radius + 1):
            points.add((point[0] + i, point[1] - i))
        # right to down
        point = (self.x + self.radius + 1, self.y)
        for i in range(self.radius + 1):
            points.add((point[0] - i, point[1] - i))
        # down to left
        point = (self.x, self.y - self.radius - 1)
        for i in range(self.radius + 1):
            points.add((point[0] - i, point[1] + i))
        # left to up
        point = (self.x - self.radius - 1, self.y)
        for i in range(self.radius + 1):
            points.add((point[0] + i, point[1] + i))
        return points


class Day15(Base):
    sensors = []
    blocked = set()
    leftest = float("inf")
    rightest = float("-inf")
    largest_radius = float("-inf")

    def preprocess_data(self):
        pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
        for line in tqdm(self.data):
            match = re.search(pattern, line)
            sensor = Sensor(match.group(1), match.group(2), match.group(3), match.group(4))
            self.blocked.add((sensor.x, sensor.y))
            self.blocked.add((sensor.beacon_x, sensor.beacon_y))
            self.sensors.append(sensor)
            self.leftest = min([self.leftest, sensor.x, sensor.beacon_x])
            self.rightest = max([self.rightest, sensor.x, sensor.beacon_x])
            self.largest_radius = max(self.largest_radius, sensor.radius)

    def puzzle1(self):
        result = 0
        for i in tqdm(range((self.leftest - self.largest_radius - 10), self.rightest + self.largest_radius + 10)):
            if "sample" in self.input_file_path:
                point = (i, 10)  # sample
            else:
                point = (i, 2000000)  # input
            if point not in self.blocked:
                flag = False
                for sensor in self.sensors:
                    if sensor.is_in_circle(point[0], point[1]):
                        flag = True
                        break
                if flag:
                    result += 1
        print(f"How many positions cannot contain a beacon? {result}")

    def test_out_of_sensor(self, point):
        if point not in self.blocked:
            flag = False
            for sensor in self.sensors:
                if sensor.is_in_circle(point[0], point[1]):
                    flag = True
                    break
            if not flag:
                print(f"What is its tuning frequency? {point[0] * 4000000 + point[1]}")
                return True
        return False

    def puzzle2(self):
        if "sample" in self.input_file_path:
            search_space = 20  # sample
        else:
            search_space = 4000000  # input

        edges = []
        for sensor in self.sensors:
            edges.append(sensor.edges)
        targets = set.union(*edges)

        for target in tqdm(targets):
            if target[0] <= search_space and target[0] >= 0 and target[1] <= search_space and target[1] >= 0:
                if self.test_out_of_sensor(target):
                    return


if __name__ == "__main__":
    obj = Day15()
    obj.run()
