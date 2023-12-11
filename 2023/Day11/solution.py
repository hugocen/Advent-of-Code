import copy


class Solution:
    def parse_data(self, data, part2=False):
        space = data.splitlines()
        for y, row in enumerate(space):
            space[y] = list(row)
        if part2:
            return space
        space = self.expand_space_horizontally(space)
        space = self.expand_space_vertically(space)
        return space

    def expand_space_horizontally(self, space):
        new_space = []
        for row in space:
            new_space.append(row)
            if len(set(row)) == 1 and row[0] == ".":
                new_space.append(copy.deepcopy(row))
        return new_space

    def expand_space_vertically(self, space):
        empty_space = []
        for x in range(len(space[0])):
            col = [row[x] for row in space]
            if len(set(col)) == 1 and col[0] == ".":
                empty_space.append(x)
        for x in reversed(empty_space):
            for y, row in enumerate(space):
                space[y].insert(x, ".")
        return space

    def get_galaxies(self, space):
        galaxies = []
        for y, row in enumerate(space):
            for x, char in enumerate(row):
                if char == "#":
                    galaxies.append((x, y))
        return galaxies

    def get_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_empty_columns(self, space):
        empty_columns = set()
        for x in range(len(space[0])):
            col = [row[x] for row in space]
            if len(set(col)) == 1 and col[0] == ".":
                empty_columns.add(x)
        return empty_columns

    def get_empty_rows(self, space):
        empty_rows = set()
        for y, row in enumerate(space):
            if len(set(row)) == 1 and row[0] == ".":
                empty_rows.add(y)
        return empty_rows

    def get_distance_to_galaxy(
        self, galaxy_a, galaxy_b, empty_rows, empty_columns, expand
    ):
        x1, y1 = galaxy_a
        x2, y2 = galaxy_b
        basic_distance = self.get_distance(galaxy_a, galaxy_b)
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2):
            if x in empty_columns:
                basic_distance += expand - 1
        for y in range(y1, y2):
            if y in empty_rows:
                basic_distance += expand - 1
        return basic_distance

    def question_1(self, data):
        space = self.parse_data(data)
        galaxies = self.get_galaxies(space)
        result = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                a = galaxies[i]
                b = galaxies[j]
                result += self.get_distance(a, b)
        return result

    def question_2(self, data, expand=1000000):
        space = self.parse_data(data, part2=True)
        galaxies = self.get_galaxies(space)
        empty_rows = self.get_empty_rows(space)
        empty_columns = self.get_empty_columns(space)
        result = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                a = galaxies[i]
                b = galaxies[j]
                result += self.get_distance_to_galaxy(
                    a, b, empty_rows, empty_columns, expand
                )
        return result
