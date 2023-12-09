class Solution:
    def get_seeds(self, line):
        seeds = []
        line = line.split(": ")[1]
        for seed in line.split(" "):
            seeds.append(int(seed))
        return seeds

    def get_seeds2(self, line):
        seeds = []
        line = line.split(": ")[1]
        line = [int(seed) for seed in line.split(" ")]
        for i in range(0, len(line), 2):
            seeds.append((line[i], line[i + 1]))
        return seeds

    def get_map(self, data):
        lines = data.splitlines()[1:]
        result = []
        for line in lines:
            line = line.split(" ")
            result.append((int(line[0]), int(line[1]), int(line[2])))
        return result

    @staticmethod
    def check_map(value, almanac):
        for dst_start, src_start, step in almanac:
            if value >= src_start and value < src_start + step:
                return dst_start + value - src_start
        return value

    @staticmethod
    def reverse_check_map(value, almanac):
        for dst_start, src_start, step in almanac:
            if value >= dst_start and value < dst_start + step:
                return src_start + value - dst_start
        return value

    @staticmethod
    def check_seeds(value, seeds):
        for seed_start, seed_step in seeds:
            if value >= seed_start and value < seed_start + seed_step:
                return True
        return False

    def walk_map(self, value, maps, idx):
        if idx == len(maps):
            return value
        return self.walk_map(self.check_map(value, maps[idx]), maps, idx + 1)

    def parse_data(self, data, part2=False):
        data = data.split("\n\n")

        if part2:
            seeds = self.get_seeds2(data[0])
        else:
            seeds = self.get_seeds(data[0])

        maps = []
        for i in range(1, len(data)):
            maps.append(self.get_map(data[i]))

        return seeds, maps

    def question_1_not_sort(self, data):
        seeds, maps = self.parse_data(data)
        dsts = []
        for seed in seeds:
            dsts.append(self.walk_map(seed, maps, 0))

        return dsts

    def reverse_walk_map(self, value, maps, idx):
        if idx == -1:
            return value
        return self.reverse_walk_map(self.reverse_check_map(value, maps[idx]), maps, idx - 1)

    def question_1(self, data):
        dsts = self.question_1_not_sort(data)

        dsts.sort()
        return dsts[0]

    def question_2(self, data):
        seeds, maps = self.parse_data(data, part2=True)
        seeds = set(seeds)

        dst = 0
        while True:
            seed = self.reverse_walk_map(dst, maps, len(maps) - 1)
            if self.check_seeds(seed, seeds):
                return dst
            dst += 1
