class Solution:
    def parse_data(self, data):
        lines = data.splitlines()
        result = []
        for line in lines:
            result.append([int(t) for t in line.split(": ")[1].split(" ") if t != ""])
        return result[0], result[1]

    def parse_data2(self, data):
        lines = data.splitlines()
        result = []
        for line in lines:
            line = line.split(": ")[1].replace(" ", "")
            result.append(int(line))
        return result[0], result[1]

    def get_possible_win(self, time, distance):
        result = 0
        for i in range(1, time - 1):
            if (time - i) * i > distance:
                result += 1
        return result

    def get_possible_win2(self, time, distance):
        start = 0
        end = 0
        for i in range(1, time - 1):
            if (time - i) * i > distance:
                start = i
                break
        for i in range(time - 1, 1, -1):
            if (time - i) * i > distance:
                end = i
                break
        return end - start + 1

    def question_1(self, data):
        times, distances = self.parse_data(data)
        result = 1
        for time, distance in zip(times, distances):
            result *= self.get_possible_win(time, distance)
        return result

    def question_2(self, data):
        times, distances = self.parse_data2(data)
        return self.get_possible_win2(times, distances)
