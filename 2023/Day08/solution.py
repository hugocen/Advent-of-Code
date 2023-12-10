import sys
from math import gcd

sys.path.append("../")
from node import Node

sys.setrecursionlimit(1500000000)


class Solution:
    def parse_data(self, data):
        lines = data.splitlines()
        instructions = lines[0]
        nodes = {}

        for line in lines[2:]:
            line = line.split(" = ")
            node_name = line[0]
            left_right = line[1].replace("(", "").replace(")", "").split(", ")
            node = Node(node_name, left_right[0], left_right[1])
            nodes[node_name] = node

        return instructions, nodes

    def walk_tree(self, node, instructions, nodes, step, part2=False):
        if part2:
            if self.is_destination(node):
                return step
        else:
            if node == "ZZZ":
                return step
        real_step = step % len(instructions)
        instruction = instructions[real_step]
        if instruction == "L":
            return self.walk_tree(
                nodes[node].go_left(), instructions, nodes, step + 1, part2
            )
        else:
            return self.walk_tree(
                nodes[node].go_right(), instructions, nodes, step + 1, part2
            )

    def walk_tree2(self, current_nodes, instructions, nodes, step):
        if step % 1000000 == 0:
            print(current_nodes, step)
        if self.is_reached_all_destination(current_nodes, nodes):
            return step
        real_step = step % len(instructions)
        instruction = instructions[real_step]
        next_nodes = []
        for node in current_nodes:
            if instruction == "L":
                next_nodes.append(nodes[node].go_left())
            else:
                next_nodes.append(nodes[node].go_right())
        return self.walk_tree2(next_nodes, instructions, nodes, step + 1)

    def get_starting_nodes(self, nodes):
        starting_nodes = []
        for node in nodes:
            if node.endswith("A"):
                starting_nodes.append(node)

        return starting_nodes

    def is_reached_all_destination(self, current_nodes, nodes):
        for node in current_nodes:
            if not node.endswith("Z"):
                return False
        return True

    def is_destination(self, node):
        return node.endswith("Z")

    def question_1(self, data):
        instructions, nodes = self.parse_data(data)
        return self.walk_tree("AAA", instructions, nodes, 0)

    def question_2(self, data):
        instructions, nodes = self.parse_data(data)
        starting_nodes = self.get_starting_nodes(nodes)
        fastest_stops = []
        for starting_node in starting_nodes:
            fastest_stops.append(
                self.walk_tree(starting_node, instructions, nodes, 0, True)
            )
        lcm = 1
        for fastest_stop in fastest_stops:
            lcm = lcm * fastest_stop // gcd(lcm, fastest_stop)
        return lcm
