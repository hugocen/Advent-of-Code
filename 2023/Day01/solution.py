import re


class Solution:
    number_strings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def pick_numbers_in_string(self, string):
        return [int(c) for c in string if c.isdigit()]

    def pick_numbers_in_string_2(self, string):
        numbers = []
        for idx, c in enumerate(string):
            if c.isdigit():
                numbers.append((idx, int(c)))

        for number_string, number in self.number_strings.items():
            match = re.finditer(number_string, string)
            for m in match:
                numbers.append((m.start(), number))
        return [number for _, number in sorted(numbers)]

    def concat_int(self, a, b):
        return int(str(a) + str(b))

    def question_1(self, data):
        result = 0
        for line in data:
            numbers = self.pick_numbers_in_string(line)
            new_number = self.concat_int(numbers[0], numbers[-1])
            result += new_number
        return result

    def question_2(self, data):
        result = 0
        for line in data:
            numbers = self.pick_numbers_in_string_2(line)
            new_number = self.concat_int(numbers[0], numbers[-1])
            print(line, numbers, new_number)
            result += new_number
        return result
