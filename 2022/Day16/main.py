# fmt: off
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
    walked = {}

    def preprocess_data(self):
        for line in self.data:
            valve = Valve(line)
            self.valves[valve.name] = valve

    def get_valves_status(self):
        status = ""
        for _, valve in self.valves.items():
            status += f" {valve.name}: {valve.open} "
        return status

    def walk(self, current_valve, minute, valves):
        if minute == 0:
            return [0, valves]
        # if (current_valve.name, minute, self.get_valves_status()) in self.walked:
            # return self.walked[(current_valve.name, minute, self.get_valves_status())]
        results = []
        # release
        if current_valve.open is False:
            release_minute = minute - 1
            current_valve_release = current_valve.flow_rate * release_minute
            # results.append([current_valve_release, path])
            if release_minute >= 1:
                for valve in current_valve.lead_to:
                    new_valves = copy.deepcopy(valves)
                    new_valves[current_valve.name].open = True
                    result = self.walk(new_valves[valve], release_minute - 1, new_valves)
                    result[0] += current_valve_release
                    results.append(result)
        # not release
        for valve in current_valve.lead_to:
            new_valves = copy.deepcopy(valves)
            results.append(self.walk(new_valves[valve], minute - 1, new_valves))

        results = sorted(results, key=lambda x: x[0])
        best = results[-1]
        # print(current_valve.name, minute, best[0])
        # self.walked[(current_valve.name, minute, self.get_valves_status())] = best
        return best

    def puzzle1(self):
        print(self.walk(self.valves["AA"], 30, self.valves))


if __name__ == "__main__":
    obj = Day16()
    obj.run()
