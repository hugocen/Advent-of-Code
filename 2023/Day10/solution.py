import sys

sys.path.append("../")
from pipe import Pipe
sys.setrecursionlimit(1500000000)


class Solution:
    def parse_data(self, data):
        lines = data.splitlines()
        pipes = []
        for y, line in enumerate(lines):
            pipes.append([])
            for x, char in enumerate(line):
                pipes[y].append(Pipe(x, y, char))

        return pipes

    def get_starting_point(self, pipes):
        for y, y_pipes in enumerate(pipes):
            for x, pipe in enumerate(y_pipes):
                if pipe.shape == "S":
                    pipe.main_loop = True
                    return pipes[y][x]

    def get_possible_routes(self, pipes, starting_point):
        routes = []
        if starting_point.x - 1 >= 0 and (
            pipes[starting_point.y][starting_point.x - 1].shape == "-"
            or pipes[starting_point.y][starting_point.x - 1].shape == "L"
            or pipes[starting_point.y][starting_point.x - 1].shape == "F"
        ):
            routes.append((starting_point.x - 1, starting_point.y))
            starting_point.left = True
        if starting_point.x + 1 < len(pipes[starting_point.y]) and (
            pipes[starting_point.y][starting_point.x + 1].shape == "-"
            or pipes[starting_point.y][starting_point.x + 1].shape == "J"
            or pipes[starting_point.y][starting_point.x + 1].shape == "7"
        ):
            routes.append((starting_point.x + 1, starting_point.y))
            starting_point.right = True
        if starting_point.y - 1 >= 0 and (
            pipes[starting_point.y - 1][starting_point.x].shape == "|"
            or pipes[starting_point.y - 1][starting_point.x].shape == "7"
            or pipes[starting_point.y - 1][starting_point.x].shape == "F"
        ):
            routes.append((starting_point.x, starting_point.y - 1))
            starting_point.up = True
        if starting_point.y + 1 < len(pipes) and (
            pipes[starting_point.y + 1][starting_point.x].shape == "|"
            or pipes[starting_point.y + 1][starting_point.x].shape == "L"
            or pipes[starting_point.y + 1][starting_point.x].shape == "J"
        ):
            routes.append((starting_point.x, starting_point.y + 1))
            starting_point.down = True

        return routes

    def fill_outer_tiles(self, pipes):
        walked = set()
        for y in range(len(pipes)):
            for x in range(len(pipes[y])):
                if pipes[y][x].shape == ".":
                    if x == 0 or x == len(pipes[y]) - 1 or y == 0 or y == len(pipes) - 1:
                        s = self.walk_outer_tiles(pipes[y][x], pipes, walked)
                        walked = walked.union(s)

    def walk_outer_tiles(self, pipe, pipes, walked):
        if (pipe.x, pipe.y) in walked:
            return walked
        if pipe.shape != ".":
            return walked
        walked.add((pipe.x, pipe.y))
        pipe.enclosed = False
        if pipe.x - 1 >= 0:
            s = self.walk_outer_tiles(pipes[pipe.y][pipe.x - 1], pipes, walked)
            walked = walked.union(s)
        if pipe.x + 1 < len(pipes[pipe.y]):
            s = self.walk_outer_tiles(pipes[pipe.y][pipe.x + 1], pipes, walked)
            walked = walked.union(s)
        if pipe.y - 1 >= 0:
            s = self.walk_outer_tiles(pipes[pipe.y - 1][pipe.x], pipes, walked)
            walked = walked.union(s)
        if pipe.y + 1 < len(pipes):
            s = self.walk_outer_tiles(pipes[pipe.y + 1][pipe.x], pipes, walked)
            walked = walked.union(s)
        return walked

    def plot_points_in_polygon(self, pipes):
        for y, y_pipes in enumerate(pipes):
            in_loop_region = False
            previous = None
            for x, pipe in enumerate(y_pipes):
                if pipe.main_loop:
                    if previous:
                        if pipe.shape == "-":
                            continue
                        elif previous.shape == "F" and pipe.shape == "7":
                            previous = None
                            in_loop_region = not in_loop_region
                        elif previous.shape == "L" and pipe.shape == "J":
                            previous = None
                            in_loop_region = not in_loop_region
                        else:
                            previous = None
                    else:
                        if pipe.shape == "F" or pipe.shape == "L":
                            previous = pipe
                        else:
                            previous = None
                        in_loop_region = not in_loop_region
                else:
                    if in_loop_region:
                        pipe.enclosed = True


    def count_enclosed(self, pipes):
        count = 0
        for y in range(len(pipes)):
            for x in range(len(pipes[y])):
                if pipes[y][x].enclosed:
                    count += 1
        return count

    def walk(self, pipes, previous_pipe, pipe, step, history):
        # print(f"previous: {previous_pipe}, current: {pipe}, step: {step}")
        pipe.main_loop = True
        history.append(pipe)
        if pipe.shape == "S":
            return step, history
        next_pipe_x, next_pipe_y = pipe.next(previous_pipe.x, previous_pipe.y)
        next_pipe = pipes[next_pipe_y][next_pipe_x]
        return self.walk(pipes, pipe, next_pipe, step + 1, history)

    def question_1(self, data):
        pipes = self.parse_data(data)
        starting_point = self.get_starting_point(pipes)
        routes = self.get_possible_routes(pipes, starting_point)
        steps, history = self.walk(pipes, starting_point, pipes[routes[0][1]][routes[0][0]], 1, [])
        result = steps // 2
        if steps % 2 == 1:
            result += 1
        return result

    def question_2(self, data):
        pipes = self.parse_data(data)
        starting_point = self.get_starting_point(pipes)
        routes = self.get_possible_routes(pipes, starting_point)
        self.walk(pipes, starting_point, pipes[routes[0][1]][routes[0][0]], 1, [])
        starting_point.convert_starting_point()
        self.plot_points_in_polygon(pipes)
        self.fill_outer_tiles(pipes)
        tiles = self.count_enclosed(pipes)
        return tiles
