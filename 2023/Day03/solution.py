class Solution:
    def get_numbers(self, data):
        numbers = []
        for y, line in enumerate(data):
            number = ""
            coordinates = set()
            for x, char in enumerate(line):
                if char.isdigit():
                    coordinates.add((x, y))
                    number += char
                else:
                    if number:
                        numbers.append((int(number), coordinates))
                        number = ""
                        coordinates = set()
            if number:
                numbers.append((int(number), coordinates))
        return numbers

    def get_engine_parts(self, data):
        engine_parts = []
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if not char.isdigit() and char != ".":
                    engine_parts.append((char, x, y))
        return engine_parts

    def search_engine_part_number(self, engine_part, numbers):
        part_numbers = set()
        adjecent_coordinates = [
            (engine_part[1] - 1, engine_part[2]),
            (engine_part[1] + 1, engine_part[2]),
            (engine_part[1], engine_part[2] - 1),
            (engine_part[1], engine_part[2] + 1),
            (engine_part[1] - 1, engine_part[2] - 1),
            (engine_part[1] + 1, engine_part[2] + 1),
            (engine_part[1] - 1, engine_part[2] + 1),
            (engine_part[1] + 1, engine_part[2] - 1),
        ]

        for idx, number in enumerate(numbers):
            for coordinate in adjecent_coordinates:
                if coordinate in number[1]:
                    part_numbers.add(idx)

        return part_numbers

    def question_1(self, data):
        engine_parts = self.get_engine_parts(data)
        numbers = self.get_numbers(data)
        part_numbers = set()
        for engine_part in engine_parts:
            part_numbers = part_numbers.union(self.search_engine_part_number(engine_part, numbers))

        result = 0
        for part_number in part_numbers:
            result += numbers[part_number][0]
        return result

    def question_2(self, data):
        engine_parts = self.get_engine_parts(data)
        numbers = self.get_numbers(data)
        result = 0
        for engine_part in engine_parts:
            if engine_part[0] == "*":
                ratios = list(self.search_engine_part_number(engine_part, numbers))
                if len(ratios) == 2:
                    result += numbers[ratios[0]][0] * numbers[ratios[1]][0]

        return result