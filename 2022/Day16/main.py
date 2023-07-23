# fmt: off
import multiprocessing
from multiprocessing import pool
from multiprocessing import process
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
import re
import copy


class Valve:
    pattern = r"^Valve (\w+) has flow rate=(\d+);"

    def __init__(self, line):
        match = re.search(self.pattern, line)
        assert match
        self.name = match.group(1)
        self.flow_rate = int(match.group(2))
        line = line.replace("leads to valve ", "lead to valves ")
        lead_to_string = line.split(" lead to valves ")[1]
        self.lead_to = lead_to_string.split(", ")
        self.open = False

    def __str__(self) -> str:
        return f"Valve: {self.name}, flow rate: {self.flow_rate}, leads to: {self.lead_to}"


class Day16(Base):
    valves = {}
    positive_and_close_valves = {}

    def preprocess_data(self):
        for line in self.data:
            valve = Valve(line)
            self.valves[valve.name] = valve
            if valve.flow_rate > 0:
                self.positive_and_close_valves[valve.name] = valve

    def get_shortest_path(self, start, end):
        unvisited = copy.deepcopy(self.valves)
        visited = {}
        current = [start]
        current_distance = 0
        while True:
            new_current = []
            for valve in current:
                if valve.name == end.name:
                    return current_distance
                if valve.name not in unvisited:
                    continue
                visited[valve.name] = unvisited[valve.name]
                del unvisited[valve.name]
                for valve in valve.lead_to:
                    if valve in unvisited:
                        new_current.append(unvisited[valve])
            current = new_current
            current_distance += 1

    def get_distances(self, start, all_valves):
        visited = {}
        current = [start]
        current_distance = 0
        while True:
            new_current = []
            for valve in current:
                if valve.name in visited:
                    continue
                visited[valve.name] = current_distance
                for valve in valve.lead_to:
                    if valve not in visited:
                        new_current.append(all_valves[valve])
            current = new_current
            current_distance += 1
            if len(current) == 0:
                return visited

    def simulate_best_target(self, valve, remain_minute):
        max_result = 0
        target_valve = None
        time_taken = 0
        print(f"Simulate for {valve.name} with {remain_minute} minutes left.")
        for open_valve in self.positive_and_close_valves:
            distance = self.get_shortest_path(valve, self.valves[open_valve])
            print(f"Distance from {valve.name} to {open_valve} is {distance}")
            if distance is None:
                continue
            potential_result = (remain_minute - distance - 1) * self.valves[open_valve].flow_rate
            if potential_result > max_result:
                max_result = potential_result
                target_valve = self.valves[open_valve]
                time_taken = distance + 1
        return target_valve, max_result, time_taken

    def walk(self, current_valve, minutes, pressure):
        if minutes == 0 or len(self.positive_and_close_valves) == 0:
            return pressure
        target_valve, max_result, time_taken = self.simulate_best_target(current_valve, minutes)
        if target_valve is None:
            return pressure
        print(f"Target valve: {target_valve.name}, max result: {max_result}, time taken: {time_taken}")
        if target_valve is None:
            return pressure
        minutes -= time_taken
        pressure += max_result
        del self.positive_and_close_valves[target_valve.name]

        return self.walk(target_valve, minutes, pressure)

    def walk_all(self, current_valve, minutes, open_and_positive_valves, all_valves):
        # print(f"Walk all for {current_valve.name} with {minutes} minutes left.")
        if minutes <= 0 or len(open_and_positive_valves) == 0:
            return 0

        distances = self.get_distances(current_valve, all_valves)

        max_result = 0
        for valve in open_and_positive_valves:
            if valve not in distances:
                continue
            new_open_and_positive_valves = copy.deepcopy(open_and_positive_valves)
            del new_open_and_positive_valves[valve]
            remain_time = minutes - distances[valve] - 1
            potential_result = remain_time * all_valves[valve].flow_rate
            potential_result += self.walk_all(all_valves[valve], remain_time, new_open_and_positive_valves, all_valves)
            if potential_result > max_result:
                max_result = potential_result

        return max_result

    def walk_all_parallel(self, current_valve, minutes, open_and_positive_valves, all_valves):
        if minutes <= 0 or len(open_and_positive_valves) == 0:
            return 0

        distances = self.get_distances(current_valve, all_valves)

        max_result = 0


        return max_result

    def puzzle1(self):
        print(self.walk_all(self.valves["AA"], 30, self.positive_and_close_valves, self.valves))

    def puzzle2(self):
        print(self.walk_all_parallel(self.valves["AA"], 30, self.positive_and_close_valves, self.valves))


if __name__ == "__main__":
    multiprocessing.freeze_support()
    obj = Day16()
    obj.run()
