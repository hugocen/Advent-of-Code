# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
import re
import multiprocessing as mp
from tqdm import tqdm
from itertools import repeat


class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = int(x)
        self.y = int(y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.radius = abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)

    def is_in_circle(self, x, y):
        return abs(x - self.x) + abs(y - self.y) <= self.radius


class Day15(Base):
    sensors = []
    blocked = set()
    leftest = float("inf")
    rightest = float("-inf")
    largest_radius = float("-inf")

    def preprocess_data(self):
        pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
        for line in self.data:
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
        for i in range((self.leftest - self.largest_radius - 10), self.rightest + self.largest_radius + 10):
            # point = (i, 10)  # sample
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

    @staticmethod
    def test_out_of_sensor(i, search_space, sensors, blocked):
        for j in range(search_space + 1):
            point = (i, j)
            if point not in blocked:
                flag = False
                for sensor in sensors:
                    if sensor.is_in_circle(point[0], point[1]):
                        flag = True
                        break
                if not flag:
                    print(f"What is its tuning frequency? {point[0] * 4000000 + point[1]}")
                    return

    def puzzle2(self):
        # search_space = 20  # sample
        search_space = 4000000  # input

        # process_pool = []

        # for i in range(search_space + 1):
        #     # self.test_out_of_sensor(point)
        #     process_pool.append(
        #         Process(
        #             target=self.test_out_of_sensor,
        #             args=(
        #                 i,
        #                 search_space,
        #                 self.sensors,
        #                 self.blocked,
        #             ),
        #         )
        #     )

        # for process in process_pool:
        #     process.start()
        # for process in process_pool:
        #     process.join()
        print(f"cpu cpunt: {mp.cpu_count()}")
        inputs = zip(range(search_space + 1), repeat(search_space), repeat(self.sensors), repeat(self.blocked))
        process_pool = mp.Pool(mp.cpu_count())
        process_pool.starmap(
            self.test_out_of_sensor,
            tqdm(inputs, total=search_space + 1),
        )


if __name__ == "__main__":
    obj = Day15()
    obj.run()
