from tqdm import tqdm

class Solution:
    def __init__(self):
        self.count_memoization = {}
        self.check_springs_memoization = {}

    def parse_data(self, data, part2=False):
        lines = data.splitlines()
        records = []
        for line in lines:
            if part2:
                line = self.get_record2(line)
            records.append(self.get_record(line))
        return records

    def count_springs(self, springs):
        if springs in self.count_memoization:
            return self.count_memoization[springs]
        count = []
        idx = len(springs) - 1
        encountered_space = False
        while idx >= 0:
            if springs[idx] == ".":
                encountered_space = True
            if springs[idx] == "#" and encountered_space:
                count = self.count_springs(springs[: idx + 1])[:]
                break
            idx -= 1
        c = springs[idx + 1 :].count("#")
        if c > 0:
            count.append(c)
        self.count_memoization[springs] = count
        return count

    def check_springs(self, springs, damages):
        current = self.count_springs(springs)
        for c, d in zip(current, damages):
            if c > d:
                return False
        return True

    def check_precise_springs(self, springs, damages):
        current = self.count_springs(springs)
        if len(current) != len(damages):
            return False
        for c, d in zip(current, damages):
            if c != d:
                return False
        return True


    def guess(self, springs, idx, damages):
        if not self.check_springs(springs[:idx], damages):
            return 0
        # print(springs, idx)
        result = 0
        for i in range(idx, len(springs)):
            if springs[i] == "?":
                new_spring_1 = springs[:i] + "#" + springs[i + 1 :]
                new_spring_2 = springs[:i] + "." + springs[i + 1 :]
                result += self.guess(new_spring_1, i+1, damages)
                result += self.guess(new_spring_2, i+1, damages)
                return result

        if self.check_precise_springs(springs, damages):
            return 1
        return 0

    def get_record(self, line):
        line = line.split(" ")
        springs = line[0]
        damages = [int(damage) for damage in line[1].split(",")]
        return (springs, damages)

    def get_record2(self, line):
        line = line.split(" ")
        springs_string = "?".join([line[0] for _ in range(5)])
        damages_string = ",".join([line[1] for _ in range(5)])
        new_line = springs_string + " " + damages_string
        return new_line

    def question_1(self, data):
        records = self.parse_data(data)
        result = 0
        for record in tqdm(records):
            result += self.guess(record[0], 0, record[1])
        return result

    def question_2(self, data):
        records = self.parse_data(data, part2=True)
        result = 0
        for record in tqdm(records):
            self.count_memoization = {}
            result += self.guess(record[0], 0, record[1])
        return result
