# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on
import copy
import math


class Monkey:
    def __init__(self, lines):
        self.number = None
        self.items = []
        self.operation = ""
        self.test_target = None
        self.items = []
        self.test_true_monkey = None
        self.test_false_monkey = None
        self.inspect_time = 0
        self.relief = True
        self.all_monkeys_test_target_prod = None
        self.set_number(lines[0])
        self.set_item(lines[1])
        self.set_operation(lines[2])
        self.set_test_target(lines[3])
        self.set_test_monkeys(lines[4:])

    def set_number(self, line):
        self.number = int(line.replace("Monkey ", "").replace(":", ""))

    def set_item(self, line):
        items_string = line.split(": ")[1]
        items = items_string.split(",")
        for item in items:
            self.items.append(int(item))

    def set_operation(self, line):
        self.operation = line.split("new = ")[1]

    def set_test_target(self, line):
        self.test_target = int(line.split("divisible by ")[1])

    def set_test_monkeys(self, lines):
        self.test_true_monkey = int(lines[0].split("monkey ")[1])
        self.test_false_monkey = int(lines[1].split("monkey ")[1])

    def inspect_item(self, item):
        old = item
        result = eval(self.operation)
        result = result % self.all_monkeys_test_target_prod
        if self.relief:
            return math.floor(result / 3.0)
        else:
            return result

    def test(self, item):
        remain = item % self.test_target
        return remain == 0

    def throw_item(self, item):
        if self.test(item):
            return self.test_true_monkey
        else:
            return self.test_false_monkey

    def receive_items(self, items):
        self.items += items

    def action(self):
        result = []
        for item in self.items:
            self.inspect_time += 1
            inspected_item = self.inspect_item(item)
            throw_target = self.throw_item(inspected_item)
            result.append((throw_target, inspected_item))
        self.items = []
        return result

    def set_all_monkeys_test_target_prod(self, all_monkeys_test_target_prod):
        self.all_monkeys_test_target_prod = all_monkeys_test_target_prod


class Day11(Base):
    monkeys = []
    origin_monkeys = []

    def preprocess_data(self):
        all_monkeys_test_target_prod = 1
        for i in range(0, len(self.data), 7):
            monkey = Monkey(self.data[i : i + 7])
            all_monkeys_test_target_prod *= monkey.test_target
            self.monkeys.append(monkey)
        for monkey in self.monkeys:
            monkey.set_all_monkeys_test_target_prod(all_monkeys_test_target_prod)
        self.origin_monkeys = copy.deepcopy(self.monkeys)

    def reset_data(self):
        self.monkeys = copy.deepcopy(self.origin_monkeys)

    def monkey_process(self):
        for monkey in self.monkeys:
            results = monkey.action()
            for result in results:
                self.monkeys[result[0]].receive_items([result[1]])

    def get_monkey_business(self):
        inspect_time = []
        for monkey in self.monkeys:
            inspect_time.append(monkey.inspect_time)
        inspect_time.sort()
        return inspect_time[-1] * inspect_time[-2]

    def puzzle1(self):
        for _ in range(20):
            self.monkey_process()
        monkey_business = self.get_monkey_business()
        print(
            f"What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? {monkey_business}"
        )

    def puzzle2(self):
        for monkey in self.monkeys:
            monkey.relief = False
        for _ in range(10000):
            self.monkey_process()
        monkey_business = self.get_monkey_business()
        print(f"What is the level of monkey business after 10000 rounds? {monkey_business}")


if __name__ == "__main__":
    obj = Day11()
    obj.run()
