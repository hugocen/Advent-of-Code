# fmt: off
import sys
sys.path.append('../')
from utils.base import Base # pylint: disable=wrong-import-position,import-error
# fmt: on


class Day10(Base):
    instructions = []

    def preprocess_data(self):
        for line in self.data:
            if line.startswith("addx"):
                instruction = line.split(" ")
                self.instructions.append((instruction[0], int(instruction[1])))
            else:
                self.instructions.append((line, 0))

    def puzzle1(self):
        target_cycle = set([20, 60, 100, 140, 180, 220])
        cycle = 0
        x_register = 1
        instruction_idx = 0
        signal_strengths_sum = 0
        in_adding = False
        while instruction_idx < len(self.instructions):
            cycle += 1
            if cycle in target_cycle:
                print(f"During Cycle: {cycle}, Register: {x_register}, Signal strength: {cycle * x_register}")
                signal_strengths_sum += cycle * x_register
            if not in_adding:
                instruction = self.instructions[instruction_idx]
                if instruction[0] == "addx":
                    in_adding = True
                else:
                    instruction_idx += 1
            else:
                x_register += self.instructions[instruction_idx][1]
                instruction_idx += 1
                in_adding = False
        print(f"What is the sum of these six signal strengths? {signal_strengths_sum}")

    def puzzle2(self):
        print("What eight capital letters appear on your CRT?")
        target_cycle = set([40, 80, 120, 160, 200, 240])
        cycle = 0
        crt_pos = 0
        x_register = 1
        instruction_idx = 0
        row = ""
        in_adding = False
        while instruction_idx < len(self.instructions):
            cycle += 1
            if crt_pos >= x_register-1 and crt_pos <= x_register+1:
                row += "#"
            else:
                row += "."
            crt_pos += 1
            if cycle in target_cycle:
                print(row)
                row = ""
                crt_pos = 0
            if not in_adding:
                instruction = self.instructions[instruction_idx]
                if instruction[0] == "addx":
                    in_adding = True
                else:
                    instruction_idx += 1
            else:
                x_register += self.instructions[instruction_idx][1]
                instruction_idx += 1
                in_adding = False


if __name__ == "__main__":
    obj = Day10()
    obj.run()
