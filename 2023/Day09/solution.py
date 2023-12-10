

class Solution:
    def parse_data(self, data):
        all_numbers = []
        for line in data.splitlines():
            line = line.split(" ")
            numbers = [int(number) for number in line]
            all_numbers.append(numbers)
        return all_numbers

    def find_differences(self, history):
        numbers = history[-1]
        if self.reach_all_zero(numbers):
            return history
        differences = []
        for i in range(len(numbers) - 1):
            differences.append(numbers[i + 1] - numbers[i])

        history.append(differences)
        return self.find_differences(history)

    def find_extrapolated_numbers(self, history, idx, part2=False):
        if part2:
            history[idx].insert(0, history[idx][0] - history[idx+1][0])
        else:
            history[idx].append(history[idx][-1] + history[idx+1][-1])

    def find_all_extrapolated_numbers(self, history, part2=False):
        for idx in range(len(history) - 2, -1, -1):
            self.find_extrapolated_numbers(history, idx, part2)

    def reach_all_zero(self, numbers):
        number_set = set(numbers)
        return len(number_set) == 1 and 0 in number_set

    def question_1(self, data):
        all_numbers = self.parse_data(data)
        result = 0
        for numbers in all_numbers:
            history = [numbers]
            history = self.find_differences(history)
            self.find_all_extrapolated_numbers(history)
            result += history[0][-1]
        return result

    def question_2(self, data):
        all_numbers = self.parse_data(data)
        result = 0
        for numbers in all_numbers:
            history = [numbers]
            history = self.find_differences(history)
            self.find_all_extrapolated_numbers(history, True)
            result += history[0][0]
        return result
