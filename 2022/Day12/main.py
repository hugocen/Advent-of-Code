# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
from collections import defaultdict
import heapq as heap


class Day12(Base):
    grid = []
    start = None
    end = None

    def preprocess_data(self):
        for i, line in enumerate(self.data):
            if "S" in line:
                self.start = (i, line.index("S"))
                line = line.replace("S", "a")
            if "E" in line:
                self.end = (i, line.index("E"))
                line = line.replace("E", "z")
            self.grid.append(line)

    def can_climb(self, i, j, target_i, target_j):
        current = self.grid[i][j]
        target = self.grid[target_i][target_j]
        return ord(current) + 1 >= ord(target)

    def get_adj(self, node):
        targets = []
        if node[0] > 0 and self.can_climb(node[0], node[1], node[0] - 1, node[1]):
            targets.append((node[0] - 1, node[1]))
        if node[0] < len(self.grid) - 1 and self.can_climb(node[0], node[1], node[0] + 1, node[1]):
            targets.append((node[0] + 1, node[1]))
        if node[1] > 0 and self.can_climb(node[0], node[1], node[0], node[1] - 1):
            targets.append((node[0], node[1] - 1))
        if node[1] < len(self.grid[node[0]]) - 1 and self.can_climb(node[0], node[1], node[0], node[1] + 1):
            targets.append((node[0], node[1] + 1))
        return targets

    def dijkstra(self):
        visited = set()
        parents_map = {}
        priority_queue = []
        node_costs = defaultdict(lambda: float("inf"))
        node_costs[self.start] = 0
        heap.heappush(priority_queue, (0, self.start))

        while priority_queue:
            _, node = heap.heappop(priority_queue)
            visited.add(node)

            for adj_node in self.get_adj(node):
                if adj_node in visited:
                    continue
                new_cost = node_costs[node] + 1
                if node_costs[adj_node] > new_cost:
                    parents_map[adj_node] = node
                    node_costs[adj_node] = new_cost
                    heap.heappush(priority_queue, (new_cost, adj_node))
        return parents_map, node_costs

    def puzzle1(self):
        _, node_costs = self.dijkstra()
        print(
            f"What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal? {node_costs[self.end]}"
        )

    def puzzle2(self):
        steps = []
        for i, line in enumerate(self.data):
            for j, c in enumerate(line):
                if c == "a":
                    self.start = (i, j)
                    _, node_costs = self.dijkstra()
                    steps.append(node_costs[self.end])
        steps.sort()
        print(f"What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal? {steps[0]}")




if __name__ == "__main__":
    obj = Day12()
    obj.run()
